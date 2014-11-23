<!-- title: Arch Linux Post Install Notes -->

These notes assume that you finished the basic install from the install live CD,
which I have notes for [here][id1]. At this point you are expected to be able to
login to the Arch system installed on the local harddrive as the root user.

## Create Low-Privilege Account ##

Login normaly as root on the console and then we will create a low-privilege
account:

    groupadd <groupname>  # The same as the new user name we will create.
    useradd -m -g <group> -G <othergroups> -s /bin/bash <username>

Assuming you want to create a new user with name `rms`, the the above values
should look like this:

1. `<groupname> = rms`
2. `<group> = rms`
3. `<othergroups> = users`
4. `<username> = rms`

New low-privilege user is created, but we want to allow this user to `sudo`:

    pacman -S sudo
    visudo

Find the line that reads `root ALL=(ALL) ALL` and right under it add the
following:

    <username> ALL=(ALL) ALL

Save the file `:wq` ... At this point you have a regular user account that you
can login with, but before that let's install a GUI ...

## Create a Non-Privileged User ##

Now it’s time to create a user for the system and also add some groups to it as
it’s not recommended to run as root.

    useradd -m -g users -G wheel,storage,power -s /bin/bash jonasg

Then set the password for this new user:

    passwd jonasg

Now we have to allow this user to do administrative tasks (assuming that we
already installed `mg` and `sudo` when we ran the `pacstrap` script above):

    EDITOR=mg visudo

Next, uncomment the following line in the sudoers file:

    %wheel ALL=(ALL) ALL

## Install X Window Server ##

To install a basic X Window GUI environment, execute the following:

    pacman -S alsa-utils xorg-server xorg-server-util xorg-xinit xorg-twm
    xorg-xclock xterm urxvt mesa xf86-video-vesa

Then you can test your X installation:

    startx

That will bring up a TWM session and you can exit by entering `exit` in one of
the XTerm instances.

## Login as the New User ##

Now you can reboot or logout from the `root` session and login as the new user.

## Install a 'Real' Desktop Environment ##

We do have a very basic install of X, but we can make it look a lot nicer by
installing a few extra packages:

    sudo pacman -S xfce4 xfce4-goodies gamin slim

Also install some nice True Type fonts:

    sudo pacman -S ttf-dejavu ttf-droid ttf-inconsolata ttf-liberation
    ttf-cheapskate ttf-bitstream-vera ttf-ubuntu-font-family

Enable a graphical login prompt:

    sudo systemctl enable slim.service

Then configure the XFCE desktop environment to start automatically from the new
login prompt:

    cp /etc/skel/.xinitrc ~/

Open the new `.xinitrc` file and uncomment the following line:

    exec startxfce4

## Reboot ##

You can now reboot the machine an use the newly installed GUI environment. The
SLIM login manager will throw you right into a XFCE session. From here you can
customize the desktop, add extra monitors and software... Some extra notes about
that can be found [here][id2] and [here][id3].


[id1]: ArchInstallNotes.html "Personal Arch Installation Notes"
[id2]: ArchSetupNotes.html "Some extra setup notes"
[id3]: ArchVBoxAdditionsNotes.html "Some extra notes on installing VBox Guest Additions"
