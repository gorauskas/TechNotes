<!-- title: Basic WGET usage examples -->

If you have ever used a relatively modern flavor of UNIX, you likely used a tool
called `wget`. It comes as a standard piece of almost every single UNIX variant,
Linux included. Here are some ways that I use it on a daily basis:

**Download file**

    wget http://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz

**Downloading files with different names**

    wget http://ftp.gnu.org/gnu/wget/{wget-1.15.tar.gz,wget-1.15.tar.gz.sig}

**Multiple downloads using different protocols**

    wget http://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz ftp://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz.sig

**Using an input file**

You can use an input file that contains a list of URLs to download, like so:

    wget -i ~/Downloads/urls-for-wget.txt

**Resume incomplete download**

Sometimes a download is interrupted in the middle. To resume a partial download
use the `-c` option, liek so:

    wget -c http://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz


**Download files in the background**

Using the option `-b` sends `wget` to the background and also saves the output
to a log file:

    wget -b ~/Downloads/wget-log.txt http://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz

**Throttling download speeds**

To limit the download speed, use the `--limit-rate` option:

    wget --limit-rate=100k http://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz

**Performing downloads with authentication**

Some sites restrict access to content by requiring a username and
password. `wget` can handle that:

    wget --user=joeschmoe --password=p4sswOrd! http://ftp.gnu.org/gnu/wget/

**More information**

Of course, you can mix and match all of these options into a single command,
like so:

    wget -c -b -a ./wget-log --limit-rate=100k http://ftp.gnu.org/gnu/wget/wget-1.15.tar.gz

You can also go much further than what I described above. The script below will
check the web page for the latest listed version of wget and then download it
and its signature file if the online version is newer than the local one.

    wget -qN $(wget -qO- http://ftp.gnu.org/gnu/wget/ \
              | grep tar | cut -d\" -f6 \
              | tail -n4 | grep gz \
              | sed "s|^|http://ftp.gnu.org/gnu/wget/|")

For more information, check online or use `man` or `info`.
