<!-- title: Arch Linux Regular Partition Scheme   -->

List the current partition structure of the hard drive on which you want to
install Arch:

    lsblk

The commands listed below assume the following:

1. The HD is accessible via `/dev/sda`,
2. We'll use a GPT partition table,
3. We'll use 4 partitions, one for BIOS boot, one for `/`, one for `/home`, and
   one for Swap space, and
4. You are using a 1TB Hard Drive.

If your setup deviates from these assumptions, then you will need to change it
accordingly.

To partition and format your drive run:

    cgdisk /dev/sda

This is a version of `cfdisk` that creates GPT partition tables. It works pretty
much like `cfdisk`. In most cases, you can ignore the warning about damages GPT
structures. Ensure that `free space` is selected in the the partition list, then
invoke the `New` action.

A quick digression... There is 2 ways that the partitioning can go at this
point, in my experience. If the `First Sector` of the new partition is set to a
default value of 2048 it means that the tool will leave 1007Kb of free space at
the front of the drive. This is fine at this point and the we will use that free
space later. If the `First Sector` of the new partition is set to a default of
value of 34 it means that you will need to allocate a small BIOS Boot partition
at the beginning of the drive with a size of 1007Kb. Below we set the BIOS boot
partition now before the other partitions.

Create a small BIOS boot partition with the following settings:

1. First Sector = default
2. Size = 1007K
3. Partition Type = ef02

Create a `/` root partition with the following settings:

1. First Sector = default
2. Size = 200G
3. Partition Type = 8300

Create a swap partition with the following settings:

1. First Sector = default
2. Size = 16G (I use the amount of physical RAM I have on the computer)
3. Partition Type = 8200

Create a `/home` partition with the following settings:

1. First Sector = default
2. Size = default - use up the remainder free space available
3. Partition Type = 8300

Now select the `Write` action in `cgdisk` and confirm by typing `yes` and then
`Quit`. Now you can check the partition structure again by running `lsblk`. We
expect to see something like this:

    NAME               SIZE       TYPE
    sda                 1TB       disk
    |- sda1           1007K       part
    |- sda2            200G       part
    |- sda3             16G       part
    \- sda4            784G       part

At this point you have a new partition table written to the disk. But to make it
useful, you will also need to create a file system in each partition. In our
example, we will leave the `/dev/sda1` BIOS boot partition untouched. Make a
usable file system for our Linux partitions:

    mkfs.ext4 /dev/sda2
    mkfs.ext4 /dev/sda4

Then create and activate the swap area:

    mkswap /dev/sda3
    swapon /dev/sda3

Check everything is nice and tight:

    lsblk /dev/sda

Now you can mount the newly created local hard disk:

    mount /dev/sda2 /mnt

You should also create a mount point for `/home` and mount it now:

    mkdir /mnt/home
    mount /dev/sda4 /mnt/home

At this point you are ready to [install the base system][arch1] with the
`pacstrap` script.


[arch1]: /linux/arch/ArchInstallNotes "My Installation Notes"
