Python autoclicker for OSX
=====

An auto clicker script for OS X made in Python.
It doesn't need any dependency, as long as you got installed XCode and the relative tools for command line.

### Launching
 - Open Terminal
 - Open System Preferences and go to the "Security & Privacy" section
 - On the "Privacy" tab, click on "Accessibility" and check "Terminal" on the list (remember, you must have Admin privileges)
 - Now, on the Terminal download the repository and launch the script:
```sh
git clone git@github.com:zeroerrequattro/python-autoclicker.git
cd python-autoclicker
python clicker.py
```

### Usage
Use the `Z` Key to toggle the autoclicking.
Use the `ESC` button to exit the application

### Known Bugs
The script will stop autoclicking after a while for an unknown reason, maybe because of memory issues.
If you refocus on the terminal window it start to autoclick again.