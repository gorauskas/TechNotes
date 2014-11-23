<!-- title: Install the Real Firefox on Debian 7 -->


If you have ever played around with the Debian distributions, you will quickly
notice that Firefox is not available as a browser and in its place is something
called IceWeasel. Here I will show you how to install the real Firefox browser
on Debian 7.

The first step is to remove the IceWeasel package if it is installed:

    $ sudo apt-get remove iceweasel

Next, we will make use of a Linux Mint package repository that target Debian
proper. To do this add the following line to you `/etc/apt/sources.list` file:

    deb http://packages.linuxmint.com debian import

Now when you update your package list you will see an error like so:

    $ sudo apt-get update
    ... a ton of output ...
    W: GPG error: http://packages.linuxmint.com debian Release: The following
    signatures couldn't be verified because the public key is not available:
    NO_PUBKEY 3EE67F3D0FF405B2

This happens because you don't have the proper key for the Linux Mint
repository. To a valid PGP key do the following:

    $ sudo gpg --keyserver pgp.mit.edu --recv-keys 3EE67F3D0FF405B2
    $ sudo gpg --export 3EE67F3D0FF405B2 > 3EE67F3D0FF405B2.gpg
    $ sudo apt-key add ./3EE67F3D0FF405B2.gpg
    $ sudo rm ./3EE67F3D0FF405B2.gpg

Now you should be able to update the package list successfully. Then what's left
to do is to install firefox and you can do that like so:

    $ sudo apt-get install firefox firefox-l10n-en-us

Enjoy firefox!
