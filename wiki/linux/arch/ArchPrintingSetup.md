<!-- title: Arch Linux Printing Setup -->

## Printing (CUPS)

At home, I have a Brother HL-2270DW laser printer. Using CUPS has always served
me pretty well, and printing a one-off document is relatively painless. To set
it up, install the following:

    sudo pacman -S brother brother-hl cups cups-pdf hplip libcups system-config-printer

I recommend skipping the config files and web interface and using an alternative
interface to CUPS, in this case, that’s system-config-printer.

You’ll need to create a new group, then add yourself to that group. Substitute
logan with your username.

    sudo groupadd lpadmin
    sudo usermod -aG lpadmin logan

Next, use emacs to edit the `/etc/cups/cups-files.conf` file to add the newly
created group to the `SystemGroup` line.

    sudo emacs /etc/cups/cups-files.conf

Before...

    # Administrator user group, used to match @SYSTEM in cupsd.conf policy rules...
    SystemGroup sys root

After...

    # Administrator user group, used to match @SYSTEM in cupsd.conf policy rules...
    SystemGroup sys root lpadmin

Next, start the systemd service for CUPS.

    sudo systemctl enable org.cups.cupsd.service

Reboot your machine, since you changed your group membership and CUPS needs
cycled.

    sudo reboot

Next, launch system-config-printer from the terminal then click on Add. If a
login box appears, enter your username and password.

Image

On the left, select Network Printer, then Find Network Printer.  On the right,
enter the IP address of the printer and click Find.

image

When the printer is found, you’ll need to choose a Connection from the box at
the bottom. Choose the connection that best represents the driver pack you
installed earlier and click Forward.

image

Give the printer a name, description, and location, then click Apply.

image

When the dialog box appears, print a test page and start praying to the printing
gods that it comes out.

image

https://www.loganmarchione.com/2014/11/arch-linux-encrypted-lvm-hardware-2/#Printing_CUPS
