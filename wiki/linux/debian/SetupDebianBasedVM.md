<!-- title: Setting up a Debian-based VM -->

This article goes over some basic installation steps to be performed when a new
Debian-based linux VM is provisioned at a cloud provider.

## Connecting to the remote host

Your cloud provider management screen will list an internet facing IP address
that you can use to access the remote system. **Always use SSH for remote
connections.**

Once you have the IP address and an SSH client, you're ready to log in via SSH. Here's how:

1. Open the terminal window or application, type the following command, and then
   press Enter. Be sure to replace the example IP address with your VM's IP
   address.

    `ssh root@123.456.78.90`

2. If the warning shown below appears, type yes and press Enter to continue
   connecting.

    `The authenticity of host '123.456.78.90 (123.456.78.90)' can't be established.
    RSA key fingerprint is 11:eb:57:f3:a5:c3:e0:77:47:c4:15:3a:3c:df:6c:d2.
    Are you sure you want to continue connecting (yes/no)?`

3. The log in prompt appears, as shown below. Enter the password you created for
   the root user.

    `root@123.456.78.90's password:`

4. The SSH client initiates the connection. You know you are logged in when the
   following prompt appears:

    `Warning: Permanently added '123.456.78.90' (RSA) to the list of known hosts.
    root@li123-456:~#`

Now you can start executing commands on your VM.

## Setting the Hostname

You'll need to set your system's hostname and fully qualified domain name
(FQDN). Your hostname should be something unique. Some people name their servers
after planets, philosophers, or animals. Note that the system's hostname has no
relationship to websites or email services hosted on it, aside from providing a
name for the system itself. Your hostname should not be "www" or anything too
generic.

Enter following commands to set the hostname, replacing plato with the hostname
of your choice:

    echo "plato" > /etc/hostname
    hostname -F /etc/hostname

If it exists, edit the file `/etc/default/dhcpcd` to comment out the
`SET_HOSTNAME` directive:

File excerpt: `/etc/default/dhcpcd`

    #SET_HOSTNAME='yes'

## Update /etc/hosts

Next, edit your `/etc/hosts` file to resemble the following example, replacing
plato with your chosen hostname, example.com with your system's domain name, and
`12.34.56.78` with your system's IP address. As with the hostname, the domain
name part of your FQDN does not necesarily need to have any relationship to
websites or other services hosted on the server (although it may if you
wish). As an example, you might host "www.something.com" on your server, but the
system's FQDN might be "mars.somethingelse.com."

File: `/etc/hosts`

    127.0.0.1        localhost.localdomain    localhost
    12.34.56.78      plato.example.com        plato

If you have IPv6 enabled on your VM, you will also want to add an entry for
your IPv6 address, as shown in this example:

File: `/etc/hosts`

    127.0.0.1                       localhost.localdomain    localhost
    12.34.56.78                     plato.example.com        plato
    2600:3c01::a123:b456:c789:d012  plato.example.com        plato

The value you assign as your system's FQDN should have an "A" record in DNS
pointing to your VM's IPv4 address. For VMs with IPv6 enabled, you should also
set up a "AAAA" record in DNS pointing to your VM's IPv6 address.

## Setting the Timezone

You can change your VM's timezone to whatever you want it to be. It may be best
to set it to the same timezone of most of your users. If you're unsure which
timezone would be best, consider using universal coordinated time or UTC (also
known as Greenwich Mean Time).

Enter the following command to access the timezone utility:

    dpkg-reconfigure tzdata

Now try entering the following command to view the current date and time
according to your server:

    date

The output should look similar to this: `Thu Feb 16 12:17:52 EST 2012.`

## Installing Software Updates

Now you need to install the available software updates for your VM's Linux
distribution. Doing so patches security holes in packages and helps protect your
VM against unauthorized access.

Enter the following commands to check for and install software updates:

    apt-get update
    apt-get upgrade --show-upgraded

Good work! Now you have an up-to-date VM running in the data center of your
choice.
