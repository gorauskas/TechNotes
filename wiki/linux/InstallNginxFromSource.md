<!-- title: Installing Nginx from Source -->

Nginx is a lightweight and high performance web server designed with the purpose
of delivering large amounts of static content quickly and with efficient use of
system resources. In contrast to the Apache HTTP server that uses a threaded or
process-oriented approach to handling requests, nginx uses an asynchronous
event-driven model which provides more predictable performance under load. This
guide will help you get nginx up and running on your Debian-base Linux VM.

## Installing nginx from the Source Distribution

Because of the rapid development of the nginx web server and recent changes to
the interface, many users of nginx compile their version of the software from
sources provided by the nginx developers. Additional benefits include the
ability to configure nginx to support additional third party modules and options
which much be set at compile time.

### Install Prerequisites

Begin by ensuring that your system's package database and installed programs are
up to date by issuing the following commands:

    apt-get update
    apt-get upgrade --show-upgraded

You will also need to install several dependent packages before proceeding with
nginx installation. Issue the following command:

    apt-get install libpcre3-dev build-essential libssl-dev

### Download and Compile nginx

The source files and binaries will be downloaded in the /opt/ directory of the
file system in this example. Check the nginx download page for the URL of the
latest stable release, and then issue the following commands to obtain it
(substituting a newer link if necessary):

    cd /opt/
    wget http://nginx.org/download/nginx-1.3.7.tar.gz
    tar -zxvf nginx*
    cd /opt/nginx*/

Now we can compile the nginx server. If you want to enable third-party modules,
append options to ./configure at this juncture. Issue the following command to
configure the build options:

    ./configure --prefix=/opt/nginx --user=nginx --group=nginx --with-http_ssl_module

When the configuration process completes successfully, you will see the
following output:

    Configuration summary
        + using system PCRE library
        + using system OpenSSL library
        + md5: using OpenSSL library
        + sha1 library is not used
        + using system zlib library

     nginx path prefix: "/opt/nginx"
     nginx binary file: "/opt/nginx/sbin/nginx"
     nginx configuration prefix: "/opt/nginx/conf"
     nginx configuration file: "/opt/nginx/conf/nginx.conf"
     nginx pid file: "/opt/nginx/logs/nginx.pid"
     nginx error log file: "/opt/nginx/logs/error.log"
     nginx http access log file: "/opt/nginx/logs/access.log"
     nginx http client request body temporary files: "client_body_temp"
     nginx http proxy temporary files: "proxy_temp"
     nginx http fastcgi temporary files: "fastcgi_temp"

To build and install nginx with the above configuration, use the following
command sequence:

    make
    make install

You will also need to create a user and group for nginx. Issue the following
command to do so:

    adduser --system --no-create-home --disabled-login --disabled-password --group nginx

Nginx is now installed in /opt/nginx.

### Monitor for Software Updates and Security Notices

When running software compiled or installed directly from sources provided by
upstream developers, you are responsible for monitoring updates, bug fixes, and
security issues. After becoming aware of releases and potential issues, update
your software to resolve flaws and prevent possible system
compromise. Monitoring releases and maintaining up to date versions of all
software is crucial for the security and integrity of a system.

Please follow the announcements, lists, and RSS feeds on the following pages to
ensure that you are aware of all updates to the software and can upgrade
appropriately or apply patches and recompile as needed:

- nginx Security Advisories
- nginx Announcements

When upstream sources offer new releases, repeat the instructions for installing
nginx, spawn-fcgi, and uWSGI, and recompile your software when needed. These
practices are crucial for the ongoing security and functioning of your system.

### Create an Init Script to Manage nginx

Before we can begin to use the nginx server, we must create a means of
controlling the daemon process. You can use our nginx init script to start,
stop, or restart nginx. Issue the following commands to download the file,
change the execution mode, and set the system to initialize nginx on boot:

    wget -O init-deb.sh http://library.linode.com/assets/1139-init-deb.sh
    mv init-deb.sh /etc/init.d/nginx
    chmod +x /etc/init.d/nginx
    /usr/sbin/update-rc.d -f nginx defaults

You can now start, stop, and restart nginx just like any other server
daemon. For example, to start the server, issue the following command:

    /etc/init.d/nginx start

Congratulations! You now have a running and fully functional HTTP server powered
by nginx. Continue reading our introduction to basic nginx configuration for
more information about using and setting up the web server.
