<!-- title: Arch Linux and Virtual Box -->


## VirtualBox host support

If you’re going to be using this Arch Linux installation as a VirtualBox host,
you’ll need the following packages installed.

    sudo pacman -S virtualbox virtualbox-guest-iso virtualbox-host-modules

You can install the qt4 optional dependency in order to use the graphical
interface which is based on Qt.

In addition, you’ll need to make sure the VirtualBox kernel modules run at
startup on your host, then add your user account to the vboxusers group.

    sudo echo -e "vboxdrv\nvboxnetadp\nvboxnetflt\nvboxpci" >> /etc/modules-load.d/virtualbox.conf
    sudo gpasswd -a $USER vboxusers
    sudo reboot

Since VirtualBox 4.0, non-GPL components have been split from the rest of the
application. These features came to be known as the Oracle Extension Pack and
can be used by installing the virtualbox-ext-oracle package from the AUR.


## VirtualBox guest support

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
