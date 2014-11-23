<!-- title: How to Change the Default Browser in Xubuntu -->

I am using Xubuntu 12.04 on my main workstation at home and for the longest time
I have been trying to make Google Chrome my default browser on that
machine. I've tried several things that didn't work or worked but would not
persist when I rebooted the machine. Well, that changed just recently...

Recently I found out that there is a configuration file at
`~/.local/share/applications/mimeapps.list` that you can change and make it
stick. Just replace all references to `firefox.desktop` with
`google-chrome.desktop`.  Here are the relevant current values:

    [Added Associations]
    x-scheme-handler/http=exo-web-browser.desktop;google-chrome.desktop;
    x-scheme-handler/https=exo-web-browser.desktop;google-chrome.desktop;
    ...
    x-scheme-handler/ftp=google-chrome.desktop;
    x-scheme-handler/chrome=google-chrome.desktop;
    text/html=google-chrome.desktop;
    application/x-extension-htm=google-chrome.desktop;
    application/x-extension-html=google-chrome.desktop;
    application/x-extension-shtml=google-chrome.desktop;
    application/xhtml+xml=google-chrome.desktop;
    application/x-extension-xhtml=google-chrome.desktop;
    application/x-extension-xht=google-chrome.desktop;

    [Default Applications]
    ...
    application/x-mimearchive=google-chrome.desktop
    ...
    x-scheme-handler/http=google-chrome.desktop
    x-scheme-handler/https=google-chrome.desktop
    x-scheme-handler/ftp=google-chrome.desktop
    x-scheme-handler/chrome=google-chrome.desktop
    text/html=google-chrome.desktop
    application/x-extension-htm=google-chrome.desktop
    application/x-extension-html=google-chrome.desktop
    application/x-extension-shtml=google-chrome.desktop
    application/xhtml+xml=google-chrome.desktop
    application/x-extension-xhtml=google-chrome.desktop
    application/x-extension-xht=google-chrome.desktop

The `...` above means that I omitted 1 or more lines for brevity. Hope this
works for you too.
