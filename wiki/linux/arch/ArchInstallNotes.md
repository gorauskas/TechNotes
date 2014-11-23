<!-- title: Arch Linux Install Notes  -->

These notes assume that you are running the latest Arch install CD, which will
provide you with a command line environment running ZSH as root. The focus of
this document has turned to ensuring a minimal viable OS for use as a Virtual
Box VM for cloning into other VMs for testing.

To get a base install of Arch Linux working, boot a new VBox VM with the latest
Arch Linux ISO and follow the below steps:

## Check Internet Connection ##

If you have a wired connection and a dynamic IP is good for you then you should
be already good to go. To check run the following:

    ping -c 3 google.com

If for some reason, you have no Internet connection at this point, you should
refer to the Arch Linux wiki and installation notes.

## Prepare Hard Disks ##

List the current partition structure of the hard drive on which you want to
install Arch:

    lsblk

The commands listed below assume the following: 1) The HD is accessible via
`/dev/sda`, 2) We'll use a BIOS boot with a GPT table, 3) We'll use 3
partitions, one for BIOS boot, one for `/`, one for `/home`, and one for Swap
space, and 4) You are using a 1TB Hard Drive. If your setup deviates from these
assumptions, then you will need to change it accordingly.

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
3. Partition Type = ef02

Create a `/` root partition with the following settings:

1. First Sector = default
2. Size = 200G
3. Partition Type = 8300

Create a swap partition with the following settings:

1. First Sector = default
2. Size = 16G (I use the amount of physical RAM I have on the computer)
3. Partition Type = 8200

Create a `/home` partition with the following settings:

1. First Sector = default
2. Size = default - use up the remainder free space available
3. Partition Type = 8300

Now select the `Write` action in `cgdisk` and confirm by typing `yes` and then
`Quit`. Now you can check the partition structure again by running `lsblk`. We
expect to see something like this:

    NAME               SIZE       TYPE
    sda                 1TB       disk
    |- sda1           1007K       part
    |- sda2            200G       part
    |- sda3             16G       part
    \- sda4            784G       part

At this point you have a new partition table written to the disk. But to make it
useful, you will also need to create a file system in each partition. In our
example, we will leave the `/dev/sda1` BIOS boot partition untouched. Make a
usable file system for our Linux partitions:

    mkfs.ext4 /dev/sda2
    mkfs.ext4 /dev/sda4

Then create and activate the swap area:

    mkswap /dev/sda3
    swapon /dev/sda3

Check everything is nice and tight:

    lsblk /dev/sda

Now you can mount the newly created local hard disk:

    mount /dev/sda2 /mnt

You should also create a mount point for `/home` and mount it now:

    mkdir /mnt/home
    mount /dev/sda4 /mnt/home

## Install the Base System ##

You should now be prepared to start the installation of the base Arch system:

    pacstrap -i /mnt base base-devel mg python2 openssh sudo grub

The above will take several minutes. After the base install finishes, you will
need to generate a `fstab` file so that the system knows what to mount at boot
time:

    genfstab -U -p /mnt >> /mnt/etc/fstab

You may use a -L above instead of -U if you prefer to use labels instead of
UUIDs. It is also good to check that the `fstab` file was generated properly:

    cat /mnt/etc/fstab

## Change Root ##

Change the root folder into the newly installed system location:

    arch-chroot /mnt /bin/bash

## Language and Location Settings ##

To set your locale and language, first open the `locale.gen` file in `mg`:

    mg /etc/locale.gen

Uncomment the line that reads:

    en_US.UTF-8 UTF-8

Then execute the following command:

    locale-gen

Also run the following commands in order to persist some settings:

    echo LANG=en_US.UTF-8 > /etc/locale.conf
    export LANG=en_US.UTF-8

## Console ##

Change the default console font to something that can handle unicode properly:

    mg /etc/vconsole.conf
    FONT=Lat2-Terminus16

The FONT line should be added to the file opened with `mg`

## Set Timezone ##

Set the timezone by creating a symbolic link to the correct ZoneInfo file:

    ln -s /usr/share/zoneinfo/UTC /etc/localtime

**Note to self:** Don't do something cute like using
`/usr/share/zoneinfo/America/Tijuana` because it will screw-up your Daylight
Savings Time settings later.

## Hardware Clock ##

Always set the hardware clock to UTC:

    hwclock --systohc --utc

## Hostname ##

Set the system hostname:

    echo <myhostname> > /etc/hostname


## Root Password ##

We first need to give a root password so we can perform administrative tasks.

    passwd

## Enable Networking ##

In order for the new system to connect to network on boot, do the
following. First find the main interface name:

    ip link

Then tell the system to start dhcp deamon automatically:

    systemctl enable dhcpcd.service

You can also find out your dynamically leased ip address like this:

    ip addr

Also start the SSH daemon automatically:

    systemctl enable sshd.service

## Configure the Boot Loader ##

We should already have `grub` installed from when we ran `pacstrap` above. To
configure `grub` for bios motherboards do the following:

    grub-install --target=i386-pc --recheck /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg

## Unmount and Reboot ##

Exit the chroot environment, dismount, and reboot

    exit
    umount -R /mnt
    reboot

## Summary ##

We are now done with the installation and configuration of Arch Linux. By
following the above steps you should now have a base Arch system. For problems
refer to the [Arch wiki][id1] or the [Beginner's Guide][id2].


[id1]: https://wiki.archlinux.org/index.php/Installation_Guide "Arch Installation Guide"
[id2]: https://wiki.archlinux.org/index.php/Beginners%27_Guide "Arch Beginners Guide"
