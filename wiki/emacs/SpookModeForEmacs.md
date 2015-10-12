<!-- title: Emacs Utility For Overloading The NSA Line Eater -->

How about this for precient tin foil hat geekery...

While reading the Emacs Elisp source for version 24.3, I stumbled upon a little
gem located at `./lisp/play/spook.el`.

This file has a created data of May, 1987. Emacs has included this program for
many years. Its purpose is to add a series of *keywords* to email just before
sending it. On the theory that the NSA monitors people's email, the keywords
would be picked up by NSA's snoop computers, causing them to waste time reading
your meeting schedule notices or other email boring to everyone but you and the
recipient.

You should try it: open Emacs and type `M-x spook` to see what happens.

From the commentary on the file itself:

> Just before sending mail, do M-x spook.
> A number of phrases will be inserted into your buffer, to help
> give your message that extra bit of attractiveness for automated
> keyword scanners.  Help defeat the NSA trunk trawler!
