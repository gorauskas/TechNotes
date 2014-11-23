<!-- title: How To Install HandBrake 0.9.9 On Debian Jessie, Debian Sid And Debian Wheezy -->


Hello Linux Geeksters. For those who don’t know, HandBrake is an open-source
multiplatform multithreaded video transcoder. It is used for converting DVD or
Bluray discs to formats like MP4, MKV, H.264, MPEG-4 or other formats. You can
also encode audio files like AAC, MP3, Flac, AC3 etc. The latest version
available is HandBrake 0.9.9. how to install HandBrake 0.9.9 on Debian Jessie,
Debian Sid and Debian Wheezy.In this article I will show you how to install
HandBrake 0.9.9 on Debian Jessie, Debian Sid and Debian Wheezy.

For Debian Sid, HandBrake 0.9.9 is available via repository, so installing it is
easy. All you have to do is:

    $ sudo sh -c 'echo "deb http://www.deb-multimedia.org sid main" >> /etc/apt/sources.list'
    $ sudo apt-get update
    $ sudo apt-get install handbrake

For Debian Jessie and Debian Wheezy, there is no deb package of HandBrake 0.9.9
available, so we have to install it from sources. Follow the above instructions
exactly, in order to get a successful installation:

Install the needed dependencies:

    $ sudo apt-get install build-essential subversion yasm build-essential autoconf libtool zlib1g-dev libbz2-dev libogg-dev libtheora-dev libvorbis-dev libsamplerate-dev libxml2-dev libfribidi-dev libfreetype6-dev libfontconfig1-dev libass-dev intltool libglib2.0-dev libdbus-glib-1-dev libgtk2.0-dev libgudev-1.0-dev libwebkit-dev libnotify-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libappindicator-dev

Get the HandBrake 0.9.9 sources from SVN and cd to the newly downloaded folder:

    $ svn checkout svn://svn.handbrake.fr/HandBrake/trunk hb-trunk
    $ cd hb-trunk

Do the needed configurations:

    $ ./configure --enable-ff-mpeg2 --enable-fdk-aac --arch=x86_64 --optimize=speed

Compile and install HandBrake 0.9.9:

    $ cd build
    $ make
    $ sudo make install
