<!-- title: Arch Linux Post Install Notes -->

These notes assume that you finished the basic install from the install live CD,
which I have notes for [here][id1]. At this point you are expected to be able to
login to the Arch system installed on the local hard drive as the root user.

## Create a Non-Privileged User ##

Now it’s time to create a user for the system and also add some groups to it as
it’s not recommended to run as root.

    useradd -m -g users -G wheel,storage,power -s /bin/bash jonasg

Then set the password for this new user:

    passwd jonasg

Now we have to allow this user to do administrative tasks (assuming that we
already installed `mg` and `sudo` when we ran the `pacstrap` script):

    EDITOR=mg visudo

Next, uncomment the following line in the sudoers file:

    %wheel ALL=(ALL) ALL

From this point on you should become the new user you just created and do
everything as that account and using `sudo`.

As an extra security item, you can also remove the root password so that no one
can login as the root user (Note: don't use `passwd -l` because the recovery
root login won't work any longer):

    passwd -d root

## Update pacman ##

Edit `/etc/pacman.conf` and uncomment `[multilib]`.

Update packages, db, and system:

    pacman -Syu

At this point you can also install some utilities that allow you to access and
install software from the AUR. There are 2 packages you will need to install by
hand in order to accomplish this task. They are `package-query` and `yaourt`.

1. Download the `package-query` tarball from [https://aur.archlinux.org/packages/package-query/](https://aur.archlinux.org/packages/package-query/)
2. Download the `yaourt` tarbal from [https://aur.archlinux.org/packages/yaourt/](https://aur.archlinux.org/packages/yaourt/)
3. Move to a temporary folder like `/tmp/aur`
4. Unpack each of them with `tar -zxf <package-name>.tar.gz`
5. Go into the `package-query` directory and build it with `makepkg -s`
6. Install `package-query` with `sudo pacman -U package-query-1.5-2-x86_64.pkg.tar.xz`
7. Repeat steps 5 and 6 above for the `yaourt` package

Remember to install `package-query` first because `yaourt` depends on it. Also
install `wget` at this point with `pacman -S wget`

## Install X Window Server ##

To install a basic X Window GUI environment, execute the following:

    pacman -S alsa-utils xorg-server xorg-server-utils xorg-xinit xorg-twm xorg-xclock xterm mesa xf86-video-vesa

Then you can test your X installation:

    startx

That will bring up a TWM session and you can exit by entering `exit` in one of
the XTerm instances.

## Install a 'Real' Desktop Environment ##

First let's install some nice True Type fonts:

    sudo pacman -S ttf-dejavu ttf-droid ttf-inconsolata ttf-liberation ttf-cheapskate ttf-bitstream-vera ttf-ubuntu-font-family

We do have a very basic install of X, but we can make it look a lot nicer by
installing a few extra packages:

    yaourt -S xfce4 xfce4-goodies gamin lightdm lightdm-webkit-greeter lightdm-webkit-theme-antergos

Enable a graphical login prompt:

    sudo systemctl enable lightdm.service

There are also a few extra packages you can install to make things look even
pruttier... Icons and themes ...

    yaourt -S gtk-engine-murrine gtk-engine-unico faenza-icon-theme faience-icon-theme faenza-xfce-blue faience-themes xfce-theme-blackbird xfce-theme-greybird xfce-theme-albatross xcursor-themes xcursor-aero xcursors-oxygen

## Virtual Box ##

If you are running Arch linux inside a Virtual Box VM, then you will want to
install the Guest Additions on the Arch system. Do that like so:

    yaourt -S virtualbox-guest-utils

The above will also install the `virtualbox-guest-modules` package, but you will
have to setup the kernel to load the drivers:

    sudo modprobe -a vboxguest vboxsf vboxvideo

Also edit the file `/etc/modules-load.d/virtualbox.conf` and add the contents:

    vboxguest
    vboxsf
    vboxvideo

You can also enable the `vboxservice` service which loads the modules and
synchronizes the guest's system time with the host. You may also want to add the
`/usr/sbin/VBoxClient-all` to the autostart section in your desktop
environment. If you are using XFCE4 this is already done for you.

## Proprietary Video Drivers ##

The Linux kernel includes open-source video drivers and support for hardware
accelerated framebuffers. However, userland support is required for OpenGL and
2D acceleration in X11.

First, identify your card:

    lspci | grep -e VGA -e 3D

You should see something like this:

    01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cape Verde XT [Radeon HD 7770/8760 / R7 250X]

You will want a proprietary driver that has better support for your
hardware. For the above card you will want to install the `catalyst` driver from
the AUR.

To configure X, you will have to create an `xorg.conf` file. Catalyst provides
its own `aticonfig` tool to create and/or modify this file. For a complete list
of aticonfig options, run:

    aticonfig --help | less

Now, to configure Catalyst. If you have only one monitor, run this:

    aticonfig --initial

## Reboot ##

You can now reboot the machine an use the newly installed GUI environment. The
LightDM login manager will throw you right into a XFCE session. From here you can
customize the desktop, add extra monitors and software...


[id1]: ArchInstallNotes.html "Personal Arch Installation Notes"
