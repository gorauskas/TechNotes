<!-- title: How to Properly Maximize the Active Emacs Frame on Startup on Windows -->

I'm an avid GNU Emacs user and I like to have the active frame maximized at
startup. This is easily done on Linux:

    (set-frame-parameter nil 'fullscreen 'maximized)

But on MS Windows this is not so trivial... Like many of you, I have to use
Windows for my daily work. I tried many different approaches to get that frame
maximized on Windows, but just recently I was able to achieve that outcome in a
reliable manner that works across many different versions of Windows.

## What worked!

In an effort to not *bury the lead*, as they say... this is what I have done
that works:

    (defun w32-maximize-frame ()
      "Maximize the current frame (windows only)"
      (interactive)
      (w32-send-sys-command 61488))

    (if (eq system-type 'windows-nt)
        (progn
          (add-hook 'window-setup-hook 'w32-maximize-frame t))
      (set-frame-parameter nil 'fullscreen 'maximized))

In the above code I address maximizing the frame in the two paltforms I use
most: Linux and Windows. I defined the function `w32-maximize-frame`, which send
the Windows message to the Emacs frame for it to maximize itself. The underlying
function `w32-send-sys-command` is well-known, but initialy it did not work for
me as I'll explain below.

The strategy that did work for Windows was to wrap the call to
`w32-send-sys-command` in a function and then add a call to it to the
`window-setup-hook`. I tested this on the 7 and 8.1 versions of desktop Windows
and on 2008 R2, 2012 versions of Windows Server and using Emacs 24.3. And if
Emacs is not running on Windows, I set the frame parameter `fullscreen` to
`maximized` for the current frame.

## What didn't work...

I started this *journey* into figuring out how to start Emacs maximized a while
back. In the begginging I would let Emacs start and then just use the maximize
button on the title bar, but then I started using things like
`initial-frame-alist` and `set-frame-*` to get the top, left and size just right
for my different screens. The problem with that approach is that I had to tweak
it for every new install of Emacs on every computer I used. It got old really
quick.

Then I found the `set-frame-parameter` trick that you can see in the code
above. But that only worked for Linux variants. At this point during my
reasearch, I have already found out about the `w32-send-sys-command` approach,
but using it on my `init.el` file directly was not working. The frame would
think itself as being maximized, and you could see that by looking at the state
of the maximize button on the top-right of the window. But visually, the window
would remain small.

Next I started using the `maxframe.el` package, but that really didn't last all
that long. I found that there were several flaws with it: First, the package
would not truly maximize the frame, but it calculates the size of the frame
based on your monitor's resolution and font face sizes and strech your frame
accordingly; Second, the package would not account for the position of my XFCE
desktop panel and place the Emacs title bar under it; And third, `maxframe.el`
would not account for a multiple monitor setup and stretch the frame across my
two monitors. So I dropped it and went back to the drawing board.

## Conclusion

It turns out that the proper way to achieve the maximize frame on startup on
Windows is to use the `window-setup-hook`. This variable is a normal hook that
Emacs runs after handling the initialization files. It turns out that with the
previous approaches, I was trying to send a message in Windows to an Emacs frame
that didn't yet exist. This hook is used for setting up communication with the
windowing system and creating the initial window and is, therefore, the proper
place, or point in time, to maximize our frame in Windows.
