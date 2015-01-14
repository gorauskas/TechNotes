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

You can now take one of two paths for setting up your disks. You can either
setup a regular set of partitions or setup LVM partitions on LUKS. The former
method sets up _plain text_ or unencrypted partitions. The latter method sets up
encrypted partitions that require a key to open every time the system reboots.

1. [Regular partition scheme][archdisk1]
2. [Encrypted partition scheme][archdisk2]

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

## Setup Script ##

You need to do a bunch of setup stuff on the new system now. These tasks include:

1. Language and Location Settings
2. Console font
3. Setting the Timezone
4. Setting the Hardware Clock
5. Setting the hostname
6. Enabling networking by default
7. ... and finally, setting the root password

Luckly for you, I created a quick script to accomplish all of the above in one
fell swoop. Just do the following:

    cd /tmp
    wget -c http://gorauskas.biz/arch-setup.sh
    chmod +x arch-setup.sh
    ./arch-setup.sh

## Configure the Boot Loader ##

You should already have `grub` installed from when we ran `pacstrap` above.
This is now one of the most crucial pieces of a new Arch installation. There are
2 different ways that you can go on this step. It all hinges on how you prepared
the hard drives above.

If you chose to use regular and unencrypted partitions, simply run the following
to configure `grub`:

    grub-install --recheck /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg

If you chose to use an encrypted hard drive scheme the setup is a little more
involved.

Edit the `/etc/mkinitcpio.conf` file and make sure that the `HOOKS` setting
looks like this:

    HOOKS="base udev autodetect modconf block keyboard encrypt lvm2 resume filesystems fsck"

Then generate the initfs:

    mkinitcpio -p linux

Edit the `/etc/default/grub` file and make sure the `GRUB_CMDLINE_LINUX` looks
like this:

    GRUB_CMDLINE_LINUX="cryptdevice=/dev/sda3:lvm root=/dev/system/root resume=/dev/system/swap"

Remember that things have to match _your_ actual setup. The above matches the
names we gave things when we setup our disks above. Now you are ready to
generate the GRUB config file:

    grub-install --recheck /dev/sda
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

[archdisk1]: /linux/arch/ArchRegularPartitionScheme "Arch Linux Regular Partition Scheme"
[archdisk2]: /linux/arch/ArchEncryptedPartitionScheme "Arch Linux Encrypted Partition Scheme"
