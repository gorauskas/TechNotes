<!-- title: Configuring and Using Chrony -->

I use Network File System (NFS) on my Linux systems to share some disk space
among many machines on my network. NFS is a distributed file system protocol
originally developed by Sun Microsystems in 1984, allowing a user on a client
computer to access files over a network much like local storage is
accessed.

NFS doesn't synchronize time between client and server, and offers no mechanism
for the client to determine what time the server thinks it is. What this means
is that a client can update a file, and have the timestamp on the file be either
some time long in the past, or even in the future, from its point of view.

While this is generally not an issue, if clocks are a few seconds or even a few
minutes off, it can be confusing and misleading to humans. Of even greater
importance is the effect this has on programs. Programs often do not expect time
differences like this, and may end abnormally or behave strangely, as various
tasks timeout instantly, or take an extraordinarily long while to timeout.

Poor time synchronization also makes debugging problems difficult, because there
is no easy way to establish a chronology of events. This is especially
problematic when investigating security issues, such as break in attempts.

The workaround is to use Network Time Protocol (NTP) religiously. Use of NTP can
result in machines that have extremely small time differences. Note: The NFS
protocol version 3 does have support for the client specifying the time when
updating a file, but this is not widely implemented. Additionally, it does not
help in the case where two clients are accessing the same file from machines
with drifting clocks.

Rather than use the `ntpd` or the Network Time Protocol daemon, I opted to use a
much simpler and easier to use implemention: Chrony. Chrony implements the NTP
protocol and can act as either a client or a server. I use them as both. Here's
how I'm doing it...

First, install `chrony` ... In Debian, simple run the following command

    $ sudo apt-get install chrony

There are 2 main programs that come with `chrony`: the client and the server or
`chronyc` and `chronyd` respectively. `chronyd` is a daemon which runs in
background on the system. It obtains measurements via the network of the system
clock’s offset relative to time servers on other systems and adjusts the system
time accordingly. `chronyc` provides a user interface to chronyd for monitoring
its performance and configuring various settings. It can do so while running on
the same computer as the chronyd instance it is controlling or a different
computer.

All of my systems use both `chronyc` and `chronyd`. I have one server that
looks to the Internet for its time source and all other machines point to this
one server for their sources. You can achive this setup via configuration. THe
first thing you need to setup is the external servers you are going to point
to. Here's what I am using:

    server 0.arch.pool.ntp.org iburst
    server 1.arch.pool.ntp.org iburst
    server 2.arch.pool.ntp.org iburst

    server 0.debian.pool.ntp.org iburst minpoll 8
    server 1.debian.pool.ntp.org iburst minpoll 8
    server 2.debian.pool.ntp.org iburst minpoll 8
    server 3.debian.pool.ntp.org iburst minpoll 8

And then all other servers on my network use the following:

    server 10.0.0.92

The above IP is my Chrony time server. Here are some of the other most
interesting configuration items for Chrony:

1. The `driftfile` stores the computer's clock gain/loss rate in parts per
   million.

        driftfile /var/lib/chrony/drift

2. The program called `chronyc` can configure aspects of `chronyd` operation
   once it is running. You can protect it with a password stored in the keys
   file.  You also need to tell `chronyd` which numbered key in the file is used
   as the password for `chronyc`.

        keyfile /etc/chrony.keys
        commandkey 2

3. If you want to act as an NTP server for other computers. You might be running
   `chronyd` on a machine that has a LAN sitting behind it with several
   computers on it. By default, chronyd does not allow any clients to access it.
   You need to explicitly enable access using `allow` and `deny` directives.

        allow 10.0.0.0/24

4. You may also want `chronyd` to act as a NTP broacast server. This means that
   a broadcast packet is sent to the broadcast address every 60 seconds.  The ip
   address MUST correspond to the broadcast address of one of the network
   interfaces on your machine.

        broadcast 60 10.0.0.255

5. If you want to present your computer's time for others to synchronise with,
   even if you don't seem to be synchronised to any NTP servers yourself, enable
   the following line in the config file. The value 10 may be varied between 1
   and 15.  You should avoid small values because you will look like a real NTP
   server.  The value 10 means that you appear to be 10 NTP 'hops' away from an
   authoritative source (atomic clock, GPS receiver, radio clock etc).

        local stratum 10

6. Beyond the above settings, you can also set the values for log and PID files,
   allow remote management, etc.

You may also want to interract with your `chronyd` server in real-time, and you
can do that with the `chronyc` program. By calling simply `chronyc` on the
command line you will connect to the local host. If you want to connect to a
remote `chronyd` host, runt he following command:

    $ chronyc -h 10.0.0.92

The above connects you to the `chronyd` server and presents a prompt where you
can enter commands. Here are some of the most common sommands and their
meanings:

1. `password`: Provide password needed for most commands
2. `activity`: Check how many NTP servers/peers are online/offline
3. `clients`: Show clients that have accessed the server
4. `makestep`: Immediately correct the system clock instead of slewing
6. `online`: Warn that connectivity to a source has been restored
7. `sources`: Display information about the current set of sources
8. `sourcestats`: Display the rate & offset estimation performance of sources
9. `tracking`: Display system clock performance

For further informatin and more detailed documentation go to
[Chrony home][link1].


[link1]: http://chrony.tuxfamily.org/ "Chrony home"
