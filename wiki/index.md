<!-- title: Home -->

To see the complete list of pages in this wiki, you can browse the
[directory listing][link2].

## Linux

Linux is my OS of choice these days. I use it as a server to host my projects
and as my primary OS on my workstation at home and at work. Here are some notes:

* [Install Nginx from Source][linux1]
* [Linux Kernel Source Screensaver][linux2]
* [Install &amp; Connect to PostgreSQL][linux3]
* [PostgreSQL Remote Management][linux4]
* [SystemD For Administrators][linux5]
* [Configuring and Using Chrony][linux6]
* [Renew IP Lease][linux7]

### Arch Linux

The notes on installing Arch Linux below are an amalgamation and a condensation
of the content that already exists in the Arch Install Guide and the Arch
Wiki. Please refer to those resources if there are problems.

* [Installation Notes][arch1]
* [Post-Install Notes][arch2]
* [Arch on the Pi][arch3]
* [Pacman key issues on Linode][arch4]
* [Arch Linux Encrypted Partition Scheme][arch5]
* [Arch Linux Regular Partition Scheme][arch6]
* [Enable Wifi Network from CLI][arch7]
* [Arch Linux and Virtual Box][arch8]

### Debian Linux

Various notes on working with Debian-based VMs

* [Setting up a VM][debian1]
* [Securing a VM][debian2]
* [Running XFCE 4.10][debian3]
* [Install the Real Firefox][debian4]
* [Install Handbrake][debian5]
* [Install Kept Back Packages][debian6]

## Code

Notes about programming and computer science

* [So, you want to write your own language?][code1]
* [REST API Guidance][code2]

### Java

* [Check number primality using Java 8 Streams][java1]
* [Get a prime number sequence using Java 8 Streams][java2]

### CSharp

* [List Comprehensions in CSharp][csharp1]

### Python

* [Time-Saving Tips for Python][python1]

## Tools

Many notes on the various tools that I use:

* [Basic WGET usage examples][tools1]
* [Hand Brake CLI reference][tools2]
* [Burn ISO to USB][tools3]
* [Resume interrupted downloads with cURL in Linux][tools4]
* [Virtual Box Fails to Start Virtual Machine][tools5]
* [Smash into Vim][tools6]

### GIT

git is a distributed version control system. What follows are notes about my
preffered workflows, feature details and genereal tips & tricks:

* [Workflows][git1]
* [Aliases][git2]
* [Using git Under CygWin in Windows][git3]
* [Github Flow][git4]
* [Migrating Git Repos][git5]

### Emacs

Various notes about how to use and configure GNU Emacs. I love this quote from
Neal Stephenson about his use of emacs:

> emacs outshines all other editing software in approximately the same way that
> the noonday sun does the stars. It is not just bigger and brighter; it simply
> makes everything else vanish.

... and also this quote from [Phil Hagelberg][link1]:

> I do as much as I can in GNU Emacs since it pains me to use monolithic
> software that can't be modified at runtime. Emacs is the closest you can get
> on a modern OS (except maybe for Smalltalk) to the dream of the fully-dynamic
> Lisp Machines of the 80s - you can alter nearly any aspect at runtime without
> recompiling or even restarting. Also worth mentioning is that you use the same
> mechanisms in your extensions as the original authors use in writing it in the
> first place. It's hard to overstate the benefits of this setup. It's like the
> shift from punch cards to interactive operating systems. When the friction of
> tweaking your environment drops below a certain point, you can take advantage
> of positive feedback loops and become more likely to experiment and improve
> things that wouldn't be worthwhile in a more conventional OS.

... and here are the notes themselves:

* [Build & Install Emacs from Source on Ubuntu 13.04][emacs1]
* [Emacs Utility For Overloading The NSA Line Eater][emacs2]
* [Maximize the Active Emacs Frame on Startup on Windows][emacs3]

## Other Stuff

Various other interesting notes...

* [Install Faenza Icon Theme][other1]
* [How to Change the Default Browser in Xubuntu][other2]
* [Three Rules for Project Selection][other3]
* [Running a Linksys WRT54GL with DD-WRT behind an AT&amp;T UVerse 2Wire Gateway][other4]
* [When your boss says hello at the urinal...][other5]


[arch1]: /linux/arch/ArchInstallNotes "My Installation Notes"
[arch2]: /linux/arch/ArchPostInstallNotes "My Post Installation Notes"
[arch3]: /linux/arch/ArchLinuxOnRaspberryPi "Arch on a Raspberry Pi"
[arch4]: /linux/arch/PacmanKeyIssuesOnLinode "Pacman key issues on Linode"
[arch5]: /linux/arch/ArchEncryptedPartitionScheme "Arch Linux Encrypted Partition Scheme"
[arch6]: /linux/arch/ArchRegularPartitionScheme "Arch Linux Regular Partition Scheme"
[arch7]: /linux/arch/EnableWifiNetworkFromCLI "Enable Wifi Network from CLI"
[arch8]: /linux/arch/ArchVirtualBox "Arch linux and VirtualBox"

[debian1]: /linux/debian/SetupDebianBasedVM "Setup a Debian-based VM"
[debian2]: /linux/debian/SecuringYourDebianBasedVM "Securing your Debian-based VM"
[debian3]: /linux/debian/Debian7WithXfce4.10 "Running XFCE 4.10 on Debian"
[debian4]: /linux/debian/InstallRealFirefoxOnDebian7 "Install the real Firefox on Debian"
[debian5]: /linux/debian/HandbrakeOnDebian "Install Handbrake on Debian"
[debian6]: /linux/debian/DebianKeptBackPackages "Install Kept Back Packages"

[linux1]: /linux/InstallNginxFromSource "Installing Nginx from Source"
[linux2]: /linux/LinuxKernelSourceScreeSaver "Linux Kernel Source Screensaver"
[linux3]: /linux/InstallConnectPostgres "Install &amp; connect to PostgreSQL"
[linux4]: /linux/PostgreSQLRemoteManagement "PostgreSQL Remote Management"
[linux5]: /linux/SystemD4Admins "SystemD For Administrators"
[linux6]: /linux/ConfigureChrony "Configuring and Using Chrony"
[linux7]: /linux/RenewIPLease "Renew IP Lease"

[emacs1]: /tools/emacs/BuildInstallEmacsFromSourceUbuntu1304 "Building & Installing Emacs"
[emacs2]: /tools/emacs/SpookModeForEmacs "Emacs Utility For Overloading The NSA Line Eater"
[emacs3]: /tools/emacs/MaximizingEmacsFrameOnStartupOnWindows "Maximize the Active Emacs Frame on Startup on Windows"

[git1]: /tools/git/GitWorkflow "Git Workflows for JGG"
[git2]: /tools/git/GitAliases "Useful Git Aliases"
[git3]: /tools/git/GitOnCygwinNote "Git on Cygwin"
[git4]: /tools/git/GithubFlow "Github Flow"
[git5]: /tools/git/MigratingGitRepos "Migrating Git Repos"

[tools1]: /tools/WgetUsageExamples "Basic WGET usage examples"
[tools2]: /tools/HandBrakeCliReference "Hand Brake CLI reference"
[tools3]: /tools/BurnIsoToUsb "Burn ISO to USB"
[tools4]: /tools/ResumeInterruptedDownloadsWithCurl "Resume interrupted downloads with cURL in Linux"
[tools5]: /tools/VBoxFailsToStartVM "Virtual Box Fails to Start Virtual Machine"
[tools6]: /tools/SmashIntoVIM "Smash into Vim"

[code1]: /code/WriteYourOwnLanguage "So, you want to write your own language?"
[code2]: /code/RestApiGuidance "REST API Guidance"

[java1]: /code/java/CheckNumberPrimalityUsingJavaStreams "Check number primality using Java 8 Streams"
[java2]: /code/java/GetPrimeSequenceUsingJavaStreams "Get a prime number sequence using Java 8 Streams"

[csharp1]: /code/csharp/ListComprehensionsInCSharp "List Comprehensions In CSharp"

[python1]: /code/python/TimeSavingTipsForPython "Time-Saving Tips for Python"

[other1]: /other/InstallFaenzaIconTheme "Install Faenza Icons"
[other2]: /other/ChangingDefaultBrowser "How to Change the Default Browser in Xubuntu"
[other3]: /other/ThreeRulesForProjectSelection "Three Rules for Project Selection"
[other4]: /other/LinksysWRT54GLBehind2Wire "Linksys behind 2Wire"
[other5]: /other/WhenYourBossSaysHello "When your boss says hello..."

[link1]: http://technomancy.us/ "Technomancy"
[link2]: /_list "Directory listing"
