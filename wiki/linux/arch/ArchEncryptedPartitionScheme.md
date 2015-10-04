<!-- title: Arch Linux Encrypted Partition Scheme   -->

## Prelude

Before starting, let's discuss some of the design decisions I made:

1. I chose to go with a traditional BIOS instead of UEFI. My motherboard does
   support UEFI, but since this a stationary workstation under my desk, and
   since I am yet to figure out how to make UEFI work under Linux, I decided to
   go with old school BIOS.
2. I chose to go with a GUID Partition Table (GPT) instead of a Master Boot
   Record (MBR). GPT allows for more flexibility than MBR.
3. Both BIOS boot and `/boot` need to be on their own, unencrypted partitions.
4. Filesystem of choice is Ext4.
5. I use LVM to manage a logical volume that I'll encrypt.
6. I use the Linux Unified Key Setup or LUKS, using dm-crypt as the disk
   encryption backend.

Second, let's review some of the assumptions I made in this document:

1. The hard disk is accessible via `/dev/sda`. The likelyhood that your drive
   will be mapped to adifferent device is really high. Adjust accordingly!
2. You are using a 1 TB hard drive. If your HD size is different than adjust
   accordingly.
3. I assume that you are installing Arch Linux. Some of the technical details
   may work on other linux distributions, but your mileage will definitely
   vary.

Now that this stuff is out of the way, let's begin with the real work...

## Wipe your disk

When rebuilding a system, I always wipe the disk before doing anything. If your
HD is large then this step can take a long time. If your disk is already
encrypted, you can get away with simply wiping the LUKS header. If you are
paranoid, then securely wipe the entire drive by using this command:

    dd if=/dev/zero of=/dev/sda iflag=nocache oflag=direct bs=4096

*NOTE:* The above command will hose your system beyond repair. Do your due
diligence of backups and other data retention techniques. You've been warned! If
you fuck up your system, it's on you.

## Identify disks

List the current partition structure of the hard drive on which you want to
install Arch:

    lsblk

Note the device your HD is mapped to.

## Setup partitions

Before I do anything, I need to ensure that the device mapper and encryption
modules are loaded into the kernel with the following command:

    modprobe -a dm-mod dm_crypt

To partition and format your drive run:

    cgdisk /dev/sda

This is a version of `cfdisk` that creates GPT partition tables. It works pretty
much like `cfdisk`. In most cases, you can ignore the warning about damaged GPT
structures. Ensure that `free space` is selected in the the partition list, then
invoke the `New` action.

A quick digression... There is 2 ways that the partitioning can go at this
point, in my experience. If the `First Sector` of the new partition is set to a
default value of 2048 it means that the tool will leave 1007Kb of free space at
the front of the drive. This is fine at this point and the we will use that free
space later. If the `First Sector` of the new partition is set to a default of
value of 34 it means that you will need to allocate a small BIOS Boot partition
at the beginning of the drive with a size of 1007Kb. Below we set the BIOS boot
partition now before the other partitions.

Create a small BIOS boot partition with the following settings:

1. First Sector = default
2. Size = 1007K
3. Partition Type = EF02

Create a partition to be mounted at `/boot` with the following settings:

1. First Sector = default
2. Size = 512M
3. Partition Type = 8300 (linux)

Create a large partition for the LVM, LUKS encrypted volumes:

1. First Sector = default
2. Size = default (or all remaining free space)
3. Partition Type = 8E00 (LVM)

Now select the `Write` action in `cgdisk` and confirm by typing `yes` and then
`Quit`. Now you can check the partition structure again by running `lsblk`. We
expect to see something like this:

    NAME               SIZE       TYPE
    sda                 1TB       disk
    |- sda1           1007K       part
    |- sda2            512M       part
    |- sda3            999G       part

At this point you have a new partition table written to the disk.

## Setup encryption

The type of setup I use on my Arch systems is called [LVM on LUKS][arch1]. This
means that I will setup and encrypted volume first, and then I put the logical
volumes inside it.

Now I need to create the crypto container for the larger LVM partition:

    cryptsetup -v -y -c aes-xts-plain64 -s 512 -h sha512 -i 5000 --use-random luksFormat /dev/sda3

The above means the following:

1. `cryptsetup` - manage plain dm-crypt and LUKS encrypted volumes
2. `-v` = verbose
3. `-y` = verify password, ask twice, and complain if they don’t match
4. `-c` = specify the cipher used
5. `-s` = specify the key size used
6. `-h` = specify the hash used
7. `-i` = number of milliseconds to spend passphrase processing (if using anything more than sha1, must be great than 1000)
8. `–use-random` = which random number generator to use
9. `luksFormat` = to initialize the partition and set a passphrase
10. `/dev/sda3` = the partition to encrypt

I use the below command to review the LUKS header information I just created:

    cryptsetup luksDump /dev/sda3

It's always good to copy this information and save it in a safe place.

Finally, we need to unlock the LUKS device before we can setup LVM on it. This
will mount the device at `/dev/mapper/crypto`.

    cryptsetup luksOpen /dev/sda3 crypto

## Setup LVM

First I scan for disks that are capable of hosting a physical volume:

    lvmdiskscan

### Setup physical volume

The decrypted container is now available at `/dev/mapper/crypto`. So now I need to
create a Physical Volume on top of the opened LUKS container:

    pvcreate /dev/mapper/crypto

I can see the new Physical Volume with the command:

    pvdisplay

### Setup volume group

Now I create a Volume Group named `vg00`, adding the previously created
physical volume to it:

    vgcreate vg00 /dev/mapper/crypto

I can see the volume group with the command:

    vgdisplay

### Setup logical volumes

And finally I create the Logical Volumes on the volume group:

    lvcreate -C y -L 8G vg00 -n lv_swap
    lvcreate -L 100G vg00 -n lv_root
    lvcreate -l +100%FREE vg00 -n lv_home

Of note in the above commands are the following parameters:

1. `-C y`: toggles the contiguous allocation policy for logical volumes
2. `-L`: the  size  to  allocate for the new logical volume
3. `-l`: the number of logical extents to allocate for the new logical volume
4. `-n`: the name for the new logical volume

I can see the logical volumnes with the command:

    lvdisplay

The last thing I need to do in setting up LVM is to scan for volume groups and
import any changes:

    vgscan
    vgchange -ay

## Create and mount filesystems

To make all of this disk setup useful, I will also need to create a file system
in the `/boot` partition. In our example, I will leave the `/dev/sda1` BIOS boot
partition untouched (it doesn't need a filesystem) and make an usable filesystem
for our `/boot` partition:

    mkfs.ext4 /dev/sda2

Now I need to format the file system on each of the logical volumes:

    mkswap -L swap /dev/vg00/lv_swap
    mkfs.ext4 -L root /dev/vg00/lv_root
    mkfs.ext4 -L home /dev/vg00/lv_home

Now you can mount the newly created local hard disk:

    mount /dev/vg00/lv_root /mnt

You should also create a mount point for `/boot` and `/home` and mount them now:

    mkdir /mnt/{boot,home}
    mount /dev/sda2 /mnt/boot
    mount /dev/vg00/lv_home /mnt/home

And last, turn on swap:

    swapon /dev/vg00/lv_swap

Check everything is nice and tight:

    lsblk /dev/sda

At this point you are ready to [install the base system][arch2] with the
`pacstrap` script.


[arch1]: https://wiki.archlinux.org/index.php/Dm-crypt/Encrypting_an_entire_system#LVM_on_LUKS "LVM on LUKS"
[arch2]: /linux/arch/ArchInstallNotes "My Installation Notes"
