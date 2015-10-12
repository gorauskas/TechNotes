<!-- title: Some Notes on Using Git with Cygwin on Windows -->


Just recently I rebuilt a system that I use for work. After I installed Cygwin
on it, I started getting some weird errors when using git with ssh to do some
source control tasks.

When doing a fetch, pull or push to/from origin, or really any git command that
uses ssh to communicate, the ssh client would complain with the error:

    Could not create directory '/home/jgg/.ssh'.
    The authenticity of host 'github.com (204.232.175.90)' can't be established.
    RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
    Are you sure you want to continue connecting (yes/no)?

Once I enter `yes`, I get the following:

    Failed to add the host to the list of known hosts (/home/ME/.ssh/known_hosts).

This was happening everytime I was using git under cygwin and very quickly the
situation became completely unsustainable. But after doing a little research, I
found a solution that is pretty simple:

1. Locate the `passwd` file, which is usually at `C:\cygwin\etc\`
2. Open it with your prefered editor
3. On the line that starts with your username, change the section that reads
   `/home/ME` to read `/cygdrive/c/path/to/home/folder/ME` or wherever your home
   folder is.
4. Save the changes and restart the Cygwin Terminal

Expect to see the authenticity check one final time and see the ssh client
actually be able to write to the `known_hosts` file.
