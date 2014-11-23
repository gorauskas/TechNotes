<!-- title: Debian: Install Packages that were Kept Back -->

Have you ever seen this message when updating your Debian-based system: "The
following packages have been kept back"? Here's why you see it and how to
solve it:

You just tried to run the following command:

    $ sudo apt-get update && sudo apt-get upgrade --show-upgraded -y

... and you get the message:

    The following packages have been kept back

Running `apt-get dist-upgrade` is dangerous for a stable environment. The wrong
`source.list` setting and you end up with a broken Debian. You might get the
entire application upgraded to a version you don't want. For example, the kernel
upgrade is kept back. You just want to upgrade the kernel, not the entire
distribution.

A better way to handle a *kept back* package is:

1. `sudo aptitude`
2. If you have kept back package you should see Upgradable Packages on top of
   the list.
3. Hit `+` on that list
4. Hit `g` twice
5. Answer debconf stuff if asked
6. Press `return` to continue
7. Press `Q` to quit
8. Press `yes`

The *kept back* packages are now installed.
