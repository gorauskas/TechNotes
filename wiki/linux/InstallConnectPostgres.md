<!-- title: Install PostgreSQL and connect to it remotely -->

These are my notes on how to install PostgreSQL (version 9 or above) on a Debian
based system and then connect to it using pgAdmin from a second remote machine.

## Install PostgreSQL

To install PostgreSQL on a Debian-based system run this command:

    $ sudo apt-get install postgresql postgresql-contrib

Then create a database and user with privileges.

    $ sudo su - postgres
    postgres@pgserver:~$ createdb mydb
    postgres@pgserver:~$ createuser -P
    Enter name of role to add: mydb_user
    Enter password for new role:
    Enter it again:
    Shall the new role be a superuser? (y/n) n
    Shall the new role be allowed to create databases? (y/n) n
    Shall the new role be allowed to create more new roles? (y/n) n
    postgres@pgserver:~$ psql
    psql (9.1.9)
    Type "help" for help.

    postgres=# GRANT ALL PRIVILEGES ON DATABASE mydb TO mydb_user;
    GRANT
    postgres=# \q
    postgres@pgserver:~$ logout

The machine hosting the database is called `pgserver` and we will refer to it by
that name from now on.

## Enable remote access to PostgreSQL

By default, PostgreSQL remote access is disabled for security reasons, but
sometimes we need to access our databases remotely for development purposes or
from a web server. Here's what we need to do to enable remote access:

Open an SSH connection to the `pgserver` machine:

    ssh user@pgserver

Once connected we will need to edit the PostgreSQL client authentication
configuration file located at `/etc/postgresql/9.1/main/pg_hba.conf` with our
editor of choice. Find a line similar to the one below:

    host      all     all    127.0.0.1/32           md5

In PostgreSQL 9.1.9, the line above is preceed by the comment `IPv4 local
connections`. This default configuration will only allow connections from the
localhost. In my isntallation, I changed this configuration to allow only
machines in my local subnet, so any machine with an IP address with the pattern
`10.0.0.*` will be able to connect. Below is what my new configuration looks
like:

    host      all     all    10.0.0.0/24            trust

Make sure to use the proper IP range for our network. Save and close the
`pg_hba.conf` file.

## Enable networking for PostgreSQL

Also by default, PostgreSQL TCP/IP networking capabilities are turned off and
we'll need to enable them in order to connect to `pgserver` remotely. Open a
configuration file called `/etc/postgresql/9.1/main/postgresql.conf` and find a
line that starts with `listen_addresses` and a value of `localhost` should be
assigned to it by default. We need to change that line to look like this:

    listen_addresses='*'

This will allow PostgreSQL to listen on all available IP addresses on our
`pgserver` machine. Save and close the file.

## Restart the PostgreSQL server

To make the configuration changes we made above take we need to restart the
database server, which can be accomplished with the following command:

    sudo /etc/init.d/postgresql restart

At this point, everything should be working fine and you should be able to
connect from the remote system to `pgserver`. Unless, of course, you are
paranoid like me and run a firewall on the `pgserver` machine.

## IPTables firewall rules

Refer to the notes on [Securing your Debian-based VM][link1] for more details
specific to IPTables configuration. So we also need to make sure that IPTables
is not blocking our remote connection to `pgserver` by editing a configuration
file. On our systems we use the file `/etc/iptables.firewall.rules` for our
IPTables configuration and this may be different on other systems.

We need to add the following 2 lines to this file:

    -A INPUT -p tcp -s 10.0.0.90 --sport 1024:65535 -d 10.0.0.91 --dport 5432 -m state --state NEW,ESTABLISHED -j ACCEPT
    -A OUTPUT -p tcp -s 10.0.0.91 --sport 5432 -d 10.0.0.90 --dport 1024:65535 -m state --state ESTABLISHED -j ACCEPT

The lines above will open port 5432, which is the standard port the PostgreSQL
server listens on, but it will only allow communication to go through back and
forth between 2 machines. The `pgserver` machine has the IP `10.0.0.91` in the
above example and the client workstation has IP `10.0.0.90`. After saving this
configuration we will have to reload it into our firewall:

    sudo iptables-restore < /etc/iptables.firewall.rules

We can also run the following command to validate our firewall settings:

    sudo iptables -L

## Using pgAdmin to connect remotely

There are really great open source tools for managing and developing for
PostgreSQL. One of them is pgAdmin, which we can install via `apt-get` in a
Debian based ditribution. To install it on our remote workstation, enter the
following command:

    sudo apt-get install pgadmin3

Now that we have it installed, we can start it and from the File menu we can
choose the Add Server command and enter the necessary information into the New
Server Registration dialog box. Then click OK and you should be connected to the
remote `pgserver` machine.

![New Server Registration](http://farm3.staticflickr.com/2870/10241805134_19a8e97813_o.png)

[link1]: http://gorauskas.org/SecuringYourDebianBasedVM.html "Securing your Debian-based VM"
