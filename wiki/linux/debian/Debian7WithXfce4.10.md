<!-- title: Running XFCE 4.10 on Debian 7.4 -->

The Debian 7 series (a.k.a. Wheezy or stable) repositories are currently serving
the `xfce4` package at version 4.8 and the upgrade to XFCE 4.10 series is not
slated to occur until the next major version relase, known as Jessie or testing
currently. But I want to use XFCE 4.10 now...

Luckly, there is a way for me to pick and choose certain packages from
different Debian repositories, while still maintaining proper dependencies. So,
here's how I installed it on Debian 7:

1. First I installed the latest Debian stable with a default XFCE desktop. This
   is version 7.4 at the time of this writing. I got it
   [here](http://cdimage.debian.org/debian-cd/7.4.0/amd64/iso-cd/debian-7.4.0-amd64-xfce-CD-1.iso).
2. I installed it with the Desktop, SSH, and Base System options checked.
3. Next I booted the new Debian 7 system and logged in. I had a default Debian
   install with XFCE 4.8 desktop.
4. Next I edited my `sources.list` file like so:

    `sudo <editor-of-choice> /etc/apt/sources.list`

5. And inserted the following repository at the bottom of the `sources.list` file:

    `deb http://ftp.us.debian.org/debian/ testing main`

6. I also had to ensure that the default release in the Apt system remained
   configured to use `wheezy`. I created a file like so:

    `sudo <editor-of-choice> /etc/apt/apt.conf.d/30default-release`

7. In that file I inserted the following directive:

    `APT::Default-Release "wheezy";`

8. I saved and closed the files above and then ran the following:

    `sudo apt-get update`

9. Then I was able to install XFCE 4.10 by issuing the following command:

    `sudo apt-get -t testing install xfce4 xfce4-terminal`

## Recap

This is what I have done so far: I installed Debian 7 with the default XFCE 4.8
desktop. I edited the `sources.list` file to add a reference to the Debian
testing repository. I made sure that the default Apt repository remained the
stable one. Then I updated the Apt system and installed XFCE 4.10 from testing.

Note that with the `-t` option, `apt` will track the package in the given
release until the package version or newer is available in default release.

## Let's Make it Look Better

At this point, I logged out and then back in and I had the new XFCE 4.10 desktop
available. But that's not quite enough. I wanted to make it look better by
installing a good looking theme. My personal favorite theme for XFCE is
[Greybird](http://shimmerproject.org/project/greybird/).

Let's dispense with the fluff and get down to just the stuff:

    sudo apt-get install gtk-engine-murrine
    mkdir ~/.themes
    cd ~/Downloads/
    git clone https://github.com/shimmerproject/Greybird
    cp -R Greybird ~/.themes

Then I used XFCE *Settings Manager* to set the *Appearance* and the *Window
Manager* settings to use the new Greybird theme.

I also installed the Faenza icon theme:

    mkdir ~/Downloads/faenza
    cd ~/Downloads/faenza
    wget http://faenza-icon-theme.googlecode.com/files/faenza-icon-theme_1.3.zip
    unzip faenza-icon-theme_1.3.zip
    sudo ./INSTALL

Running as sudo will install the theme globally in `/usr/share/icons`. Also
ensure that the permissions on the Faenza folders under `/usr/share/icons` is
properly set to `drwxr-xr-x`.

That's it... Enjoy!
