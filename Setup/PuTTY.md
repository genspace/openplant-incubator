### Who is this for?
If you start to manage many Raspberry Pi's it might be work getting an SSH client, such as PuTTY

Running the ssh pi@raspberrypi.local command to connect to multiple Raspberry Pi's can cause errors if you:
- have multiple Raspberry Pi's
- change OS's frequently (by flashing the card and connecting again)
- change the Wifi network
- OR, are under an active network intrusion (please be sure to change your password IMMEDIATELY upon setting up your Raspberry Pi the first time, this the minimum you can do to protect yourself)

Example
![Rpi0W-SSH warning-DNS spoofing](https://user-images.githubusercontent.com/12764347/93722967-bc260400-fb68-11ea-952d-1778dc04c493.png)

Windows users: [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- Choose 64-bit if your OS can support it, if you're not sure what you have, it's fine to use 32-bit then
- Under Package Files > MSI: Choose the 64-bit files if your OS can support it, if you're not sure what you have, it's fine to use 32-bit then

Open up the PuTTY program > type in the IP address (or try all of them if you have multiple results returned from ping) > open
  - It will give you a warning, select "Yes"

![PuTTY](https://helpdesk.it.helsinki.fi/sites/default/files/styles/full_content/public/thumbnails/image/putty_asetukset_2.jpg?itok=XLqXacVj)

Saving your IP address for future use:
1. You need to be in the "Session" category (default) on the left
2. Enter the IP address of your Raspberry Pi here
3. Name your session
     - I would suggest something descriptive such as "Rpi0W-OpenPlant-192.xxx.xx.xxx", this way you know what project it is and what IP address it was in case you need to check against a list of multiple IP addresses if you have many Raspberry Pi's
      - In any case this makes future access as simple as opening PuTTY and double clicking the "name" you've given it, so make sure you can recognize it
4. Click Save
      - It will now populate the empty white box left of the save button with your named session
     - From now on you can just double click that name to reconnect 
  
