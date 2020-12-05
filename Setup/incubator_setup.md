This part is specifically for Genspace NYC's OpenPlant group, and it assumes you have the hardware all setup and connected (Rpi0 + PCB + camera + LED's).
This will then install the software needed to operate aforementioned components. 

SSH onto your Rpi0 and run this command:

```
pip3 install git+https://github.com/genspace/openplant-incubator
```

Then run 
```
incubate-me
```

If this is your first time installing a python package onto your pi, you may need to run the following command if the Raspberry Pi is unable to locate the `incubate-me` command:

```
source ~/.profile
```

The `incubate-me` command will prompt you for a password to decrypt secrets needed to connect to the AWS server. You will need to get a password from the Genspace NYC's OpenPlant group and enter the value when prompted.

```
*** C L A S S I F I E D ***
```

The script will also prompt the user to enter in a set of configuration values at first start-up. You can just accept the defaults by hitting return on your keyboard, except for the `INCUBATOR_NAME` parameter. You must assign you own name for this value. No spaces should be used in this value. 

If you would like to edit the values in your configuration file at some future date, simply enter `set-config` to reconfigure the system configuration settings.

To upgrade the script to the latest version, run this command:

```
pip3 install --upgrade git+https://github.com/genspace/openplant-incubator.git
```

Optional:
- If you'd like to see the data graphically, you're going to need the URL and password from Genspace's OpenPlant group to access the Metabase 
```
*** C L A S S I F I E D ***
```

Please request access for for those resources

Tmux Setup:
- Install tmux with 
  ```
  sudo apt install tmux
  ```
- Type ```tmux``` and then hit Enter
- This will start a Tmux session to detach the session and let it continue running even if you are no longer on SSH

Tmux Useful Shortcuts & Commands:

Control + B, then press C = create new window (virtual session with 0, 1, 2, etc)

Control + B, then press # = go to that window

Control + B, then press D = detach and run in background

```tmux attach``` = bring to foreground

```exit``` = closes one of the windows, whichever one you're active in

If you try to enter tmux again through the plain tmux command it will wipe existing session and start a new one
Once you've detached the tmux you can run it in the background and allow your incubate-me command to run in the background

TODO:

Need to get it on cron/systemd/tmux to run as a background process
Need to get extra motors

