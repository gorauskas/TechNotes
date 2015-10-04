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

## Setup SSH Access ##

Once you boot Arch Linux from media into the Live Environment for installation
purposes, you are dropped into a minimal text console environment. If you have
another computer with a graphical interface, internet browser, and copy/paste
ability, then you can use SSH to install Arch remotely from that other machine.

First, I need to give `root` a password:

    passwd

Second, you need to edit the file `/etc/ssh/sshd_config` and allow SSH to login
as root:

    PermitRootLogin yes

Third, turn on the needed services:

    systemctl start sshd
    systemctl start dhcpcd

Finally, connect to the installation target from the other computer:

    ssh root@<ip-address-of-target>

## Prepare Hard Disks ##

You can now take one of two paths for setting up your disks. You can either
setup a regular set of partitions or setup LVM partitions on LUKS. The former
method sets up _plain text_ or unencrypted partitions. The latter method sets up
encrypted partitions that require a key to open every time the system reboots.

1. [Regular partition scheme][archdisk1]
2. [Encrypted partition scheme][archdisk2]

## Install the Base System ##

You should now be prepared to start the installation of the base Arch system:

    pacstrap -i /mnt base base-devel mg python2 openssh rsync curl sudo

The above will take several minutes. After the base install finishes, you will
need to generate a `fstab` file.

## Generate fstab ##

I need to generate a `fstab` file so that the system knows what to mount at boot
time:

    genfstab -U -p /mnt >> /mnt/etc/fstab

You may use a -L above instead of -U if you prefer to use labels instead of
UUIDs. It is also good to check that the `fstab` file was generated properly:

    cat /mnt/etc/fstab

Make sure to double check the UUIDs in `fstab` with the ones produces by this
command:

    blkid

**NOTE:** The last time I setup an _LVM on LUKS_ system, I ran into a situation
where I had only the main HD of the system connected during install and mapped
to `/dev/sde`. When I added other external drives, the main drive would then map
to `/dev/sdg` or something else. This caused the encrypted container to be
missed by the initial ram disk environment. The error message was _ERROR: Unable
to find root device_. The fix was to use the Live Install environment to mount
everything manually and then regenerate the Initial RamDisk environment with
`mkinitcpio` and also regenerate the Grub config. More details below.

## Change Root ##

Before doing this step, ensure that all filesystems are mounted. The _Prepare
Hard Disks_ step above addressed this, but do make sure all is mounted. Change
the root folder into the newly installed system location:

    arch-chroot /mnt /bin/bash

This is needed before I can configure the system further.

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
    curl -O http://gorauskas.biz/arch-setup.sh
    chmod +x arch-setup.sh
    ./arch-setup.sh

## Generate an Intial RamDisk ##

This step is only needed if you used disk encryption. Skip it otherwise.

Edit the `/etc/mkinitcpio.conf` file and make sure that the `HOOKS` setting
looks like this:

    HOOKS="base udev autodetect modconf block keyboard encrypt lvm2 resume filesystems shutdown fsck"

Note that the hooks _keyboard, encrypt, lvm2, and resume_ need to come after
_block_ and before _filesystems_. The _shutdown_ hook needs to come after
_filesystems_.

Finally, generate the ramdisk (iginore any errors about missing firmware):

    cd /boot
    mkinitcpio -p linux

## Configure the Boot Loader ##

Use pacman to install a few packages, including the GRUB2 bootloader.

    pacman -S fuse grub lvm2 os-prober

This is now one of the most crucial pieces of a new Arch installation. There are
2 different ways that you can go on this step. It all hinges on how you prepared
the hard drives above. If you encrypted the disks then continue from
here. Otherwise skip to _Install & Setup Grub_ below.

In the GRUB2 config file, we need to set a kernel parameter. Find the line
`GRUB_CMDLINE_LINUX=""` and add the cryptdevice parameter to specify the location
of your encrypted LVM. Edit the `/etc/default/grub` file and make sure the
`GRUB_CMDLINE_LINUX` looks like this:

    GRUB_CMDLINE_LINUX="cryptdevice=/dev/sda3:crypto root=/dev/vg00/lv_root resume=/dev/vg00/lv_swap"

Remember that things have to match _your_ actual setup. The above matches the
names I gave things when we setup my disks above.

### Install & Setup Grub

Now you are ready to install and generate the GRUB config file:

    grub-install --target=i386-pc --recheck /dev/sda
    grub-mkconfig -o /boot/grub/grub.cfg

The following warnings can be safely ignored:

    /run/lvm/lvmetad.socket: connect failed: No such file or directory
    WARNING: Failed to connect to lvmetad. Falling back to internal scanning.

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
