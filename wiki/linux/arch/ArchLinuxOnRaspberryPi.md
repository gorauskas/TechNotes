<!-- title: Installing Arch Linux on the Raspberry Pi -->

You’re going to need the following to finish this tutorial and assumes you’re
following this from a Linux Distro.

    Raspberry Pi
    Blank SD-Card 2GB or larger

First we are going to need to download the image

    wget http://archlinuxarm.org/os/ArchLinuxARM-rpi-latest.zip

Now we will need to extract the file

    unzip ArchLinuxARM-rpi-latest.zip

This will give you the latest dd image for your device the file will be
similarly named

    archlinux-hf-2013-07-22.img

The date will change as new images are updated From here you’re going to want to
insert your SD-Card that will be for the Raspberry Pi. You will want to make
sure you verify the name of your card. On my Arch Laptop my SD-Card is mmcblk0
yours may be different. If you do not use the correct one you run the risk of
overwriting import files on your system.  Now let’s copy the image onto the card

    dd bs=1M if=/path/to/archlinux-hf-2013-07-22.img of=/dev/mmcblk0

Once dd has completed you will want to eject the card. Now go ahead and place
the card into your Pi and apply your power source. First boot may take a little
time so be patient.

Your default user and password

    username: root
    password: root

Some caveats to keep in mind:

If you’re using a keyboard, mouse, or other USB devices you may need to run them
through a powered USB hub. The reason for this is the Pi’s USB port will only
handle 140mA, but the limitation has been fixed on newer boards. There is still
the possibility to run into power issues, so keep that in mind if you have
issues with devices that you’re connecting.

**References:**

- [http://jan.alphadev.net/post/53594241659/growing-the-rpi-root-partition](http://jan.alphadev.net/post/53594241659/growing-the-rpi-root-partition)
- [https://gist.github.com/Couto/3694301](https://gist.github.com/Couto/3694301)
- [http://hreikin.wordpress.com/2013/12/22/arch-linux-raspberry-pi-install-guide/](http://hreikin.wordpress.com/2013/12/22/arch-linux-raspberry-pi-install-guide/)
