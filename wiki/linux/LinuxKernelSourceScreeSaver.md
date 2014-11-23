<!-- title: Linux Kernel Source Screensaver -->


## Install linux source

    cd /usr/src
    sudo apt-get install linux-source
    sudo tar -xpjf linux-source-2.6.22.tar.bz2
    sudo ln -sf linux-source-2.6.22 linux-source

## Install xscreensaver-data-extra

    phosphor -root -delay 10000 -scale 3 -ticks 10 -program 'cat `find /usr/src/linux-source/ -name '*.c' -or -name '*.h' | sort -R | head -n 1`'
