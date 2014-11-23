<!-- title: Running a Linksys WRT54GL with DD-WRT behind an AT&amp;T UVerse 2Wire Gateway -->

For many years I have been an ADSL subscriber receiving 3 Mbps service from
AT&amp;T. The line came into the house and into a simple ADSL modem that
connected to a Linksys WRT54GL running DD-WRT firmware, which was setup to serve
as the Internet gateway for all computers in the house. I won't go into the
virtues of this particular model of Linksys router running this particular
firmware, but suffice it to say that those who know what I'm talking about will
need no further explanation.

![Linksys WRT54GL](http://farm4.staticflickr.com/3693/9032844732_c7c7d88d1d.jpg "Linksys WRT54GL")

Recently, we moved to a new house and AT&amp;T would not let me transfer the
ADSL line to the new address, but they said they would be happy to set me up
with this shinny new digital service they call UVerse. After doing some
checking, I noticed that the reviews from customers were mixed, but that the
speeds provided were pretty decent. I was leaning towards cable service, but the
wife likes AT&amp;T, so we signed up for the 12 Mbps UVerse Internet plan.

The AT&amp;T technician came to the house and set it all up in the phone box
outside &mdash; inside the house he hooked the line up to a 2Wire 3600HGV
device. When he saw my Linksys router laying nearby, he said *"With this beauty
right here..."* and he showed me the 2Wire device, *"... you won't need that
Linksys router of yours."* That should have been my fist sign that something was
amiss.

![2Wire 3600HGV](http://farm6.staticflickr.com/5341/9030618575_fa7f0fc4e4.jpg "2Wire 3600HGV")

The one redeeming quality of the 2Wire device is that it does have a really
strong radio signal, but other than that the firmware running on it is really
crippled and perhaps can do a little more than 10% of what the DD-WRT firmware
is capable of. The conspiracy theorist in me says that the 2Wire hardware and
software are probably more capable than AT&amp;T is willing to document and let
the users have access to,

Anyway, the ideal situation for me was to turn the 2Wire into a dumb modem and
use my Linksys as the gateway, just like the old ADSL days... but that was
easier in concept than in practice. There are all kinds of gotchas and tricks to
get it setup, like the *Router Behind Router* detection. After much trial and
error, I persevered, and below is the result of my research into how to get this
setup to work.

At this point I recommend that you make a backup of your current DD-WRT setup by
going to `Administration` and then the `Backup` menu and then clicking the
`Backup` button.

The first step is to get the Linksys router ready for the setup. Make sure you
can reach it and connect to it with a browser by going to
`http://192.168.1.1/`. I used an Ethernet cable directly from my laptop and into
one of the 4 LAN ports on the Linksys. Once you logged in to the Linksys, go to
`Setup` and then `Basic Setup`. Under `WAN Setup`, make sure that the
`Connection Type` is *DHCP* and give the device a unique `Router` and `Host`
name. Under the `Network Setup` area, change the `Local IP Address` to something
like `10.0.0.1` &mdash; just make sure that the IP you choose is in a different
subnet than `192.168.1.X`. With this setup we are trying to avoid conflicts
between the Linksys DHCP and the 2Wire DHCP servers and in general we want the 2
devices in separate networks anyway.

![DD-WRT WAN Setup](http://farm4.staticflickr.com/3825/9032844570_9875478076.jpg "DD-WRT WAN Setup")

The next step is to connect to the 2Wire device. I unplugged the Ethernet cable
from the Linksys and connected it to one of the LAN ports on the 2Wire. Now you
should be able to reach the 2Wire setup interface by pointing your browser to
`http://192.168.1.254/`. If at first you are unable to connect, then check your
current IP address. Since the Linksys was changed to a different network, you
may have gotten an IP in the range `10.0.0.X`. You can fix this by releasing and
renewing your IP lease. Also, in order to apply any changes to the 2Wire device
you will need to know the *System Password* which should printed on a label on
the device.

![2Wire 3600HGV Unit Back](http://farm4.staticflickr.com/3669/9030618487_19225988d5.jpg "2Wire 3600HGV Unit Back")

Before moving on, I want you to consider the above image for a moment. Here's
what's going on:

1. The blue ethernet cable connects the the 2Wire device to the WAN Port on the
   Linksys.
2. The yellow ethernet cable was used to connect the laptop directly to the
   2Wire device and also to the Linksys previously.
3. The green RJ11 cable is the digital data cable connecting to the Internet at
   large.
4. The white RJ11 cable is for the phone/voice service and goes into the
   telephone set.

![Linksys WRT54GL Back](http://farm8.staticflickr.com/7431/9030618215_a5b051692a.jpg "Linksys WRT54GL Back")

As you can see in the above image, the blue cable connected to the 2Wire device
terminates into the WAN port of the Linksys device.

Now, back from this little tangent, I was about to connect to the 2Wire device
with the browser. Once connected, go to `Settings` and the `LAN` tab and click
on the `Wireless` link and ensure that the value under `Wireless Interface` is
set to *Disabled*. I want the Linksys in charge of providing Wireless and DHCP
services. Once that's done, click the `Save` button at the bottom of the page.

![2Wire Disable Wireless](http://farm8.staticflickr.com/7400/9032844600_1a2bc85e4f.jpg "2Wire Disable Wireless")

Next I need some way for the Linksys to receive all inbound Internet traffic
into the house. This can be done by putting the Linksys in *DMZPlus* mode in the
`Firewall` setting of the 2Wire device. Go to the `Settings` tab in the 2Wire
setup interface and then click on the `Firewall` tab and click on the
`Applications, Pinholes and DMZ`. Choose the DD-WRT (or whatever name you gave
your device) from the list under `Select a computer`. Then further down on that
same settings page under `Edit firewall settings for this computer` select the
choice `Allow all applications (DMZplus mode)`. Make sure to click the `Save`
button at the bottom of this page when all done.

![Put DD-WRT in DMZPlus Mode](http://farm4.staticflickr.com/3760/9030618343_faabe08d93.jpg "Put DD-WRT in DMZPlus Mode")

You can verify that the 2Wire setup is correct by going to the `Status` page
under the `Settings` and `Firewall` sections and seeing that the *DD-WRT* device
is listed under the `Current Applications, Pinholes and DMZ Settings: Custom`
and that it was assigned a public Internet IP.

One more side bar is called for at this point in the setup process. If at any
point in time during the setup you are faced with a warning from the 2Wire
device that it has detected a *Router-Behind-Router* setup, please just ignore
it as the final outcome of the setup I am doing will render that type of
detection irrelevant. As a matter of fact, while on the 2Wire setup interface,
just go to the `Settings` tab and then the `System Info` tab and the `Event
Notifications` link and make sure that the option `Enable detection of
router-behind-router conditions` is not checked. Save your change before moving
on.

Let's do a quick recap: We first put the Linksys device in DHCP mode at the WAN
level and gave it a recognizable name, then we gave it a different subnet IP
than the default 2Wire IP. Next we disable the Wireless service on the 2Wire
device and then we put the Linksys device in DMZPlus mode in the 2Wire
configuration screens. We also verified that the Linksys is getting a public IP
from the 2Wire perspective.

![Ensure DD-WRT has Public IP](http://farm8.staticflickr.com/7282/9032844576_964df86487.jpg "Ensure DD-WRT has Public IP")

Next we need to ensure that the Linksys is getting the public IP address from
it's own perspective (see above image). Go to the `Status` tab and then the
`WAN` tab on the DD-WRT setup interface. Under the `WAN` section on that page
ensure that the `IP Address` value is the same as the one assigned to the DD-WRT
in the 2Wire interface. I obfuscated the public values here for obvious reasons.

This is where I was a little stumped when I went through these steps for the
first time. If at first your Linksys/DD-WRT doesn't recognize the public IP, try
using the `DHCP Release` button or rebooting the Linksys. I had to reboot the
Linksys twice initially, but it has been working for me without any issues for a
week now.

I hope this write up is useful to you...
