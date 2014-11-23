<!-- title: Resume interrupted downloads with cURL in Linux -->

I have recently been trying to download an ISO of a certain Linux distro, but I
find myself at the wrong end of a crappy connection. I tried downloading it with
both Firefox and Chrome but both choked very early in the process, the current
speed would go down to 0, and after a while the connection would just cutoff
with no way to resume the download from where I left off.

Fear not because [cURL][curl] comes to the rescue. After typing `Up-Arrow` and
`Enter` more time than I care to admit, I decided to let the computer do the
hard work and automate this whole thing. So I created a small Bash script called
`acurl.sh` (for Automated cURL) that looks like this:

    export ec=1;

    while [ $ec -gt 0 ];
    do
        /usr/bin/curl -O -C - $1;
        export ec=$?;
    done

    if [ $ec -eq 0 ];
        echo "Downloaded $1";
    fi

The code above expects you to pass the file to download as a parameter, which we
have in the `$1` variable. Then we tell `curl` to download it and write it to
our local disk with the same name as the remote file (this is option `-O`). We
also tell `curl` to resume a previous file download at a certain offset (this is
done via option `-C` and giving it the value `-` will allow `curl` to
automatically figure out how to resume the transfer). The next step is to
capture `curl` error codes on exit. This is done by assigning the value of `$?`
(which has the value of the most recent exit code) to our variable `$ec`. If
`$ec` is greater than 0 then we try the download with `curl` again, otherwise we
have a successful download.

Assuming that the script above is located somewhere in the `$PATH`, then using
it is as simple as this:

    acurl.sh http://distrodomain.org/downloads/linux-distro-version-platform.iso

This is definitely a brute force approach, but it does the work.

[curl]: http://curl.haxx.se/ "cURL"
