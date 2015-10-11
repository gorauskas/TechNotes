<!-- title: Renew IP Lease on Linux -->

I run a router at home with `dd-wrt`. My main machine has a static IP lease based
on the MAC address. Sometimes when I reboot the main machine the static IP is
not properly released by the DHCP subsystem and the router holds on to it,
therefore assigning my machine a regular DHCP IP.

To fix this without having to reboot the machine, follow these steps:

1. Login to the `dd-wrt` router.
2. Go to the `Setup` page and click the `Save` button followed by the `Apply`
   button. This will restart the DHCP daemon in the router without having to reboot
   it.
3. Go to the `Status` page on the router and click on the `Lan` tab and verify that
   the IP was indeed released.
4. On the main machine, run the following commands:

        sudo dhclient -v -r enp4s0
        sudo dhclient -v enp4s0

The above will renew the IP lease to the default static IP assigned to that MAC
address. Note that the above assumes you are using `NetworkManager` with
`dhclient` under it and that your network interface is `enp4s0`.
