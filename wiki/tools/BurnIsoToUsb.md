<!-- title: How do I write a CD image to a USB flash drive? -->

Several of the Debian CD and Debian Live images are created using isohybrid
technology, which means that they may be used in two different ways:

* They may be written to CD/DVD and used as normal for CD/DVD booting.
* They may be written to USB flash drives, bootable directly from the BIOS of
  most PCs.

The most common way to copy an image to a USB flash drive is to use the dd
command on a Linux machine:

    dd if=<file> of=<device> bs=4M; sync

where:

* `<file>` is the name of the input image, e.g. netinst.iso
* `<device>` is the device matching the USB flash drive, e.g. /dev/sda,
  /dev/sdb. Be careful to make sure you have the right device name, as this
  command is capable of writing over your hard disk just as easily if you get
  the wrong one!
* `bs=4M` tells dd to read/write in 4 megabyte chunks for better performance;
  the default is 512 bytes, which will be much slower
* The `sync` is to make sure that all the writes are flushed out before the
  command returns.
