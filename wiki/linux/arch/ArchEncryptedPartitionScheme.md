<!-- title: Arch Linux Encrypted Partition Scheme   -->

List the current partition structure of the hard drive on which you want to
install Arch:

    lsblk

The commands listed below assume the following:

1. The HD is accessible via `/dev/sda`,
2. We'll use a GPT partition table,
3. We'll use 3 partitions, one for `/boot`, one for a LVM encrypted volume, and
   one for BIOS boot
4. You are using a 1TB Hard Drive.

If your setup deviates from these assumptions, then you will need to change it
accordingly.

To partition and format your drive run:

    cgdisk /dev/sda

This is a version of `cfdisk` that creates GPT partition tables. It works pretty
much like `cfdisk`. In most cases, you can ignore the warning about damages GPT
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

At this point you have a new partition table written to the disk. But to make it
useful, you will also need to create a file system in the `/boot` partition. In
our example, we will leave the `/dev/sda1` BIOS boot partition untouched. Make a
usable file system for our `/boot` partition:

    mkfs.ext4 /dev/sda2

Now you will also need to create the crypto container for the larger partition:

    cryptsetup -c aes-xts-plain64 -s 512 -h sha512 -i 5000 --use-random luksFormat /dev/sda3

Follow the steps to create a passphrase. Next we need to open the crypto
container:

    cryptsetup open --type luks /dev/sda3 lvm

The decrypted container is now available at `/dev/mapper/lvm`. So now you need to
create a Physical Volume on top of the opened LUKS container:

    pvcreate /dev/mapper/lvm

Then create a Volume Group named `system`, adding the previously created
physical volume to it:

    vgcreate system /dev/mapper/lvm

And finally you create the Logical Volumes on the volume group:

    lvcreate -L 16G system -n swap
    lvcreate -L 100G system -n root
    lvcreate -l +100%FREE system -n home

Now you need to format the file system on each of the logical volumes:

    mkswap -L swap /dev/system/swap
    swapon /dev/system/swap
    mkfs.ext4 -L root /dev/system/root
    mkfs.ext4 -L home /dev/system/home

Check everything is nice and tight:

    lsblk /dev/sda

Now you can mount the newly created local hard disk:

    mount /dev/system/root /mnt

You should also create a mount point for `/boot` and `/home` and mount them now:

    mkdir /mnt/{boot,home}
    mount /dev/sda2 /mnt/boot
    mount /dev/system/home /mnt/home

At this point you are ready to [install the base system][arch1] with the
`pacstrap` script.


[arch1]: /linux/arch/ArchInstallNotes "My Installation Notes"
