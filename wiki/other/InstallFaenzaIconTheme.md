<!-- title: Install the Faenza Icon Theme -->

A very nice looking icon theme for Gnome and XFCE. Comes in a very easy to
install package. Do the following to install:

    $ cd ~/Downloads
    $ curl -O http://faenza-icon-theme.googlecode.com/files/faenza-icon-theme_1.3.zip
    $ mkdir faenza
    $ mv faenza-sources_1.3.tar.gz faenza/

Creating the directory `faenza` and moving the zip file into it before
decompressing is a good idea, otherwise `unzip` will just spread all the files
into the current Downloads folder and you will have crap everywhere... Then do
this:

    $ unzip faenza-icon-theme_1.3.zip
    $ sudo ./INSTALL

... and just follow the directions from the installation script. Running as `sudo`
will install globally and running as an unprevileged user will install in your
home directory. Enjoy!
