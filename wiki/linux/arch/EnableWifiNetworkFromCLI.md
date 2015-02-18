<!-- title: Enable Wifi Network from CLI -->

I use Arch Linux as the OS for several of my Raspberry Pies. There are times
when you need to turn on wifi after Arch is installed on the SD card. Follow
these steps to turn Wifi on:

1. Make sure you can connect to the Pi (wired connection initially)
2. SSH to the Pi and login
3. Install the following 3 packages

        $ sudo pacman -S wireless_tools wpa_supplicant dialog

4. Once the packages above as installed, you should be able to use a very nifty
   tool called:

        $ sudo wifi-menu

5. The program will scan for networks and present you with a list.
6. Pick the SSID of the network you want to connect to.
7. Enter a name for the new profile to be created.
8. Enter the security key for the connection you chose.
9. This generates the file `/etc/netctl/<profile>`
10. Now _enable_ and _start_ the new wifi network profile:

        $ sudo netctl enable <profile>
        $ sudo netctl start <profile>

Now you can safely unplug the network cable from the Pi and use the wifi
network exclusively.
