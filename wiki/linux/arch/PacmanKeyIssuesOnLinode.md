<!-- title: Pacman Key issues with Arch Linux on Linode -->

*This note is relevant to running Arch Linux on Linode VMs*

If you get asked to import maintainer keys and fail, or if you get package
corrupt errors, do the following:

1. Open the file `/etc/pacman.d/gnupg/gpg.conf`
2. Replace the keyserver line with the value: `keyserver hkp://pgp.mit.edu:11371`
3. Save and exit
4. Reset all keys with: `pacman-key --init`
5. Populate keys: `pacman-key --populate archlinux`
6. Update the system with: `pacman -Syy`
7. Upgrade the system with: `pacman -Syu`

Hope this helps and enjoy your Arch instance on Linode!
