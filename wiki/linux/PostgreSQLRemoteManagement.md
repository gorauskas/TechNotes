<!-- title: Manage your PostgreSQL Database from a Remote Workstation -->


At home I have my main development workstation and then I spin up VMs that mimic
my production environment to run different types of integration tests. One of
these VMs is running a relatively recent version of PostgreSQL. By default,
PostgreSQL is setup to allow connections coming from the local host only. In
this article I will walk through the steps of setting up PostgreSQL so that it
allows connections from other machines also.

## Setup Remote Connections

There are, essentially, two lines in two different PostgreSQL configuration
files that need to be changed to allow remote connections to work.

The first file is `postgresql.conf` and this is usually found at
`/etc/postgresql/9.1/main/` on Debian-based systems. Open that file and find the
line that starts with `listen_addresses`. By defaul the value assigned to it
should be `'localhost'`. Change that so the line reads like this:

    listen_addresses = '*'

The second file is called `pg_hba.conf`. In this file you need to look for a
IPv4 local conections line that starts with `host`. By default, the line reads
the following:

    host    all             all             127.0.0.1/32            md5

You need to change this line to read like this:

    host    all             all             10.0.0.0/24             trust

For all intents and purposes, the default is telling PostgreSQL to accept
connections only from the localhost (that's what the `/32` is for), while we are
changing the value to allow any host with an IP starting with 10.0.0.* to
connect. The above will only work after you restart PostgreSQL with the
following command:

    sudo /etc/init.d/postgresql restart

Again, YMMV if you are using anything other than Debian.

## Allowing Connections Through a Firewall

The above is really all you have to do with PostgreSQL proper to allow remote
connections. But if you are like me, you are probably running a firewall on your
systems also and you will need to punch a whole for PostgreSQL to talk through.

You can find out more about how I setup my IPTables firewall by
[reading this][firewallsetup]. In my case, I need to allow only one system (my
workstation) to connect to the VM hosting PostgreSQL. I created the following
lines in my IPTables condiguration file:

    # Allow connections to Postgres DB Server from hurricane
    -A INPUT -p tcp -s 10.0.0.90 --sport 1024:65535 -d 10.0.0.60 --dport 5432 -m state --state NEW,ESTABLISHED -j ACCEPT
    -A OUTPUT -p tcp -s 10.0.0.60 --sport 5432 -d 10.0.0.90 --dport 1024:65535 -m state --state ESTABLISHED -j ACCEPT

In the above, the first line allows traffic on port 5432 into the local system
from the `10.0.0.90` IP address, which is my development workstation. The second
line allows the local system to send traffic out via port 5432, which is the
default port used by PostgreSQL.

## Conclusion

To allow remote connections to your PostgreSQL instance, all you have to do is
edit `postgresql.conf` and `pg_hba.conf`. Also remember to address firewall configuration issues that may
arise.


[firewallsetup]: http://gorauskas.org/SecuringYourDebianBasedVM.html "Securing your Debian-based VM"
