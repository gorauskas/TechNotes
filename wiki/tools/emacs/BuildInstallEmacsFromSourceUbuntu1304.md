<!-- title: Build Emacs from Source in Ubuntu 13.04 -->

Over the years I have written several of these articles and I find that every 2
to 3 years I need to re-write these notes because the installation process
diverges enough from the previous set of steps that it warrants a re-write.

The main Linux distribution that I have settled on lately is Xubuntu, which is a
XFCE-based version of Ubuntu. I dabble in other distros also and I am
experimenting a lot lately with Arch and other Debian-based distros. One thing
is clear, the versions of GNU Emacs available with each distribution are
different. So, as a standard I will always try to download the latest stable GNU
Emacs sources and build it on the system I am using at the moment. This ensures
that I have a homogeneous set of features across the different machines and also
that I am pretty close to the bleeding edge.

In order to get to this state with your Emacs install you can follow the below
steps. These steps are focused on a Debian-based distro using APT. I will assume
that you have a base Debian or Ubuntu system already installed with a common GUI
environment. Again, I wrote these notes for a Xubuntu system running XFCE.

Let's start by downloading and installing the tools needed to build Emacs:

    $ sudo apt-get install build-essential git git-core curl automake autogen autoconf ssh

Next, you need to get the sources for Emacs. There is two ways to go about doing
this: 1) Clone the sources from an Emacs repository directly or 2) Download the
latest compressed source tarball from a FSF/GNU mirror site.

To clone the Emacs source from a repo, do the following:

    $ cd ~/Downloads
    $ git clone git://git.savannah.gnu.org/emacs.git

Cloning will take several minutes, because git will get all the history and
changes and we all know that Emacs has a *long* history. The clone method is the
way to go for those who will hack on emacs itself. The easier way to do this,
however, and the way that I prefer is to pull the source tarball from a
mirror. A list of available mirrors can be found at the [FSF site][id1]. You can
pick any of these sites and download from it. The command to do that will differ
based on the mirror you pick, but should look something like this:

    $ curl -O http://mirror.sdunix.com/gnu/emacs/emacs-24.3.tar.gz

While you are downloading the tarball or cloning the repo you should open
another terminal window and start installing some needed Emacs dependencies in
parallel:

    $ sudo apt-get install texinfo libncurses5-dev libgtk2.0-dev libgif-dev libjpeg-dev libpng-dev libxpm-dev libtiff4-dev libxml2-dev librsvg2-dev libotf-dev libm17n-dev libgpm-dev libgnutls-dev libgconf2-dev libdbus-1-dev

Once the above deps are installed and you finished retrieving the sources for
Emacs, it's time to do the actual build. Decompress the source if you downloaded
it and change directory into the Emacs source:

    $ tar -zxvf emacs-24.3.tar.gz
    $ cd ~/Downloads/emacs-24.3/

Configure the build according to what you want your installation to look like:

    $ sudo ./autogen.sh
    $ ./configure

I use the vanilla configuration, but you can change it to what suits you best
and you can view all alternatives by using `./configure --help` ... If you don't
like what `configure` has done for you (read the `configure` output) you can
also clean things up and start over with `make distclean`.

The key thing that I am trying to achieve is a message from `configure` that
looks very similar to the below output. Note all the `yes` values next to all
the stuff that `configure` checks for; this is a direct outcome of installing
all the dependency packages above. Emacs absolutely needs `texinfo`, `ncurses`,
an X toolkit and the image libraries to even build. The rest of the stuff is
nice to have, but if you don't install it you will get a `no` from `configure`
for that feature check.

    ... a ton of output

    Configured for `x86_64-unknown-linux-gnu'.

      Where should the build process find the source code?    ~/Downloads/emacs-24.3
      What compiler should emacs be built with?               gcc -std=gnu99 -g3 -O2
      Should Emacs use the GNU version of malloc?             yes
          (Using Doug Lea's new malloc from the GNU C Library.)
      Should Emacs use a relocating allocator for buffers?    no
      Should Emacs use mmap(2) for buffer allocation?         no
      What window system should Emacs use?                    x11
      What toolkit should Emacs use?                          GTK2
      Where do we find X Windows header files?                Standard dirs
      Where do we find X Windows libraries?                   Standard dirs
      Does Emacs use -lXaw3d?                                 no
      Does Emacs use -lXpm?                                   yes
      Does Emacs use -ljpeg?                                  yes
      Does Emacs use -ltiff?                                  yes
      Does Emacs use a gif library?                           yes -lgif
      Does Emacs use -lpng?                                   yes
      Does Emacs use -lrsvg-2?                                yes
      Does Emacs use imagemagick?                             no
      Does Emacs use -lgpm?                                   yes
      Does Emacs use -ldbus?                                  yes
      Does Emacs use -lgconf?                                 yes
      Does Emacs use GSettings?                               yes
      Does Emacs use -lselinux?                               no
      Does Emacs use -lgnutls?                                yes
      Does Emacs use -lxml2?                                  yes
      Does Emacs use -lfreetype?                              yes
      Does Emacs use -lm17n-flt?                              yes
      Does Emacs use -lotf?                                   yes
      Does Emacs use -lxft?                                   yes
      Does Emacs use toolkit scroll bars?                     yes

    ... more output

Now you can go into the actual build of Emacs by issuing the following command:

    $ make

And then last step is to install the Emacs you just finished building:

    $ sudo make install

... and run it:

    $ emacs &

Enjoy hacking with Emacs!

P. S. One last step that is personal and relevant to me only is to install my
Emacs configuration. Execute the following to accomplish that:

    $ rm -r .emacs.d
    $ git clone git@github.com:gorauskas/.emacs.d.git

You will of course need to have the correct encryption key in order to clone the
repo like the line above.


[id1]: http://www.gnu.org/prep/ftp.html "GNU Emacs mirror list"
