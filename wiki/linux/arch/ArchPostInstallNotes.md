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

    pacman -S alsa-utils xorg-server xorg-server-utils xorg-xinit xorg-twm xorg-xclock xterm

Then you can test your X installation:

    startx

That will bring up a TWM session and you can exit by entering `exit` in one of
the XTerm instances.

## Install a 'Real' Desktop Environment ##

We do have a very basic install of X, but we can make it look a lot nicer by
installing a few extra packages:

    yaourt -S xfce4 xfce4-goodies gamin lightdm lightdm-gtk-greeter

Enable a graphical login prompt:

    sudo systemctl enable lightdm.service

There are also a few extra packages you can install to make things look even
pruttier... Icons and themes ...

    yaourt -S gtk-engine-murrine gtk-engine-unico faenza-icon-theme
              xfce-theme-blackbird xfce-theme-greybird xfce-theme-albatross
              xcursor-themes xcursor-aero xcursors-oxygen

## Tweaks ##

### Proprietary Video Drivers

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

### Networking

First let's install some graphical networking tools:

    yaourt -S networkmanager network-manager-applet networkmanager-openvpn networkmanager-pptp

I enable the NetworkManager service to start at boot. However, by default, Arch
Linux receives an IP address via DHCP by using the DHCP client daemon
(dhcpcd). Since the two will conflict, I'm going to disable dhcpcd.

    systemctl enable NetworkManager.service
    systemctl disable dhcpcd
    systemctl disable dhcpcd@enp2s0

### Fonts

Let's install some nice True Type fonts:

    sudo pacman -S font-mathematica freetype2 terminus-font ttf-bitstream-vera
                   ttf-cheapskate ttf-dejavu ttf-droid ttf-fira-mono
                   ttf-fira-sans ttf-freefont ttf-inconsolata ttf-liberation
                   ttf-linux-libertine ttf-ubuntu-font-family xorg-xfontsel

### User directories

To create all of the default directories in $HOME (e.g., Documents, Music,
Pictures, etc...), run the two commands below.

    sudo pacman -S xdg-user-dirs
    xdg-user-dirs-update

### Codecs and DVD support

Unlike Ubuntu or Linux Mint, Arch Linux won’t support many codecs or DVD
playback out-of-the-box. The packages below should cover most of what you need
to do.

    sudo pacman -S alsa-firmware alsa-utils ffmpeg flac gst-libav
                   gst-plugins-base gst-plugins-good gstreamer gstreamer0.10
                   gstreamer0.10-ffmpeg gstreamer0.10-good-plugins lame
                   libdvdcss libdvdnav libdvdread libmpeg2 libtheora libvorbis
                   mplayer pavucontrol pulseaudio pulseaudio-alsa
                   pulseaudio-equalizer pulseaudio-gconf vlc winff x264 x265
                   xfce4-pulseaudio-plugin xvidcore

Unmute and test your speakers with the commands below. This is assuming you’re
using ALSA and have a 2.0 setup.

    amixer sset Master unmute
    speaker-test -c 2

### Packages for daily use

Here is also a list of packages I'll need for daily use:

    yaourt -S arandr bash-completion bzip2 cabextract cdrkit chrony clamav
              conkeror coreutils dropbox dropbox-cli emacs evince exaile
              exfat-utils file-roller filezilla firefox fish freerdp galculator
              gimp gksu gvfs gvfs-afc gvfs-mtp gzip hardinfo haveged htop
              ipython libreoffice libvncserver linux_logo lsb-release mc mg nmap
              ntfs-3g openssh openvpn opera p7zip pptpclient remmina rsync samba
              scrot thunar-archive-plugin thunar-media-tags-plugin thunar-volman
              tigervnc tlp tmux transmission truecrypt tumbler unace unarj unrar
              unzip util-linux viewnior vim wget x11vnc xchat xfburn zip zsh
              zsh-lovers zsh-syntax-highlighting

### Other

I have also written some documentation about Arch and Printing and [Arch and
Virtualbox][id2]. Check it out.

## Reboot ##

You can now reboot the machine an use the newly installed GUI environment. The
LightDM login manager will throw you right into a XFCE session. From here you can
customize the desktop, add extra monitors and software...


[id1]: ArchInstallNotes.html "Personal Arch Installation Notes"
[id2]: ArchVirtualBox.html "Arch Linux and Virtual Box"
