---
layout: post
title:  "Some Random Projects"
date:   2022-05-17 12:28:00 -0600
description: Random Projects
categories: Misc
---
These are just some random things I've made over time that I don't really think deserve their own page.

## Egg Demonlist:
Ever wanted to see the ugliest and most outdated website of all time? [Well now you can!](https://sites.google.com/view/egg-demonlist/home)
![Egg Demonlist](https://i.imgur.com/NrTQdmx.png "The Egg Demonlist")
*A picture of this absolute mistake*


## Setup Thing
I small set of shell scripts I made to install programs I liked faster on my laptop when I used to play with different OSes. I really don't know why anybody would ever want to use it because it probably only works on Ubuntu/Debian based distros but if you want to check out the project on GitHub you can do that [here.](https://github.com/Tristeamer/setup-thing)

Here's a guide on how to use it *(it may or may not be ripped sraight from the project's readme.md)*:

#### setup-thing
A thing I made after some googleing to install some programs on my laptop because I was tired of doing it myself. What this very simple script does is just download and install packages for you.

The ```wget``` command will download the main script (setupthing.sh) to ```/home/$USER/Desktop/```, that script will then clone a project folder to the desktop. Because of the way that these really shitty scripts were made they only work when ran from ```/home/$USER/Desktop/``` but I dont really see that as much of a problem because of how this script will probably only be used once or twice and can be quickly deleted from the desktop and can be quickly reinstalled (as it's not that big) if need be.

After that the ```chmod``` command will make the scripts as executeable.

Current known working distros: ```Ubuntu 21.10/Ubuntu 22.04``` (it may or may not work with any ```Debian``` based distro, I would like to add .rpm support in the future)

Current Supported Programs: ```Vlc, Steam, Google Chrome, Discord, Spotify, OBS, Gnome-Weather, Gnome-Maps, Minecraft, QBittorrent.```

I have no idea why you would ever want to use this as it only works for like 10 programs and its really poorly made and probably doesnt even work but if you want to go ahead.

If you actually would like to use this for whatever reason then do this:

Open a terminal
Then enter the following commands: 

1. ```cd ~/Desktop```
2. ```wget https://github.com/Tristeamer/setup-thing/releases/download/v1.1.0/setupthing.sh```
3. ```chmod u+x setupthing.sh```
4. ```./setupthing.sh```
5. ```chmod u+x /home/$USER/Desktop/setup-thing/DebInstaller/Installer.sh && chmod u+x /home/$USER/Desktop/setup-thing/PackageManager/PackageManagers.sh && chmod u+x /home/$USER/Desktop/setup-thing/Uninstaller/Uninstaller.sh && cd /home/$USER/Desktop/setup-thing```
6. ```./setup.sh```

Then hope it works.

(Also probably important to note that this was made as more of a basic educational project to try writing a shell script)

### Last updated: 05/17/22



