# Cloning Instructions

## Hardware:  
* see main repo information page
## Software:

* Clone the micro SD card using the Pi OS copy disk utility.  Use a USB-A to microUSB adapter to copy from the built in disk to the 2nd disk.
* Insert the 2nd disk into a new Raspberry Pi 4 and boot with a connected monitor, keyboard and mouse.  Expect the WiFi connection to SLAC-CADA to fail, since the device has not been registered.  Turn off the WiFi if necessary.
* Edit the rc.local file (`sudo nano /etc/rc.local`) and comment out the line which runs Capture_barcode.py on boot.  This line should only be enabled when the box is run headless (without monitor).
* Obtain the MAC address using the command prompt
* Submit an IT ticket with a request for an IP address the following details:
  * MAC Address of the RPi
  * access to SLAC-CADA
  * connectivity with epndev.slac.stanford.edu and epnprod.slac.stanford.edu on port 1521
  * connectivity with SMTPOUT.slac.stanford.edu on port 25
  * connectivity with mgmt-authproxy01 on port 3128
  * The hostname of the box.  The first box is ODTSSCAN01.  The next would be ODTSSCAN02, and so on
* Update the network settings with the new IP address on the RPi and reactivate the WiFi
* Rename the ODTS-mini-Scan folder in `/home/ryanford` to append "-old", then re-clone it to create a unique remote
  * `cd /home/ryanford`
  * `git clone https://github.com/ryanfordSLAC/ODTS-mini-Scan.git`
* Copy the config.ini and config.py files from ODTS-mini-Scan-old/Prod to ODTS-mini-Scan/Prod
* Revise config.py in the Prod folder of ODTS-mini-Scan to reflect the new hostname.
* Revise config.py to reflect the event file in /dev/input which receives data from the barcode scanner.
  * To determine which event file captures the scanner input, type `cat /proc/bus/input/devices` at a command prompt
  * Boot the box without the keyboard and mouse, then plug them in after boot up before running the command.  This will ensure the correct event address without keyboard and mouse.  For example, the event file is event0 without keyboard and mouse, and event13 with them.  Future updates may reconfigure the event to connect by device ID rather than event filename.
* Execute the config.py file to create config.ini.
* Edit the rc.local file (sudo nano /etc/rc.local) and uncomment the line which runs Capture_barcode.py on boot.  This line should be enabled when the box is run headless (without monitor).
* Edit the crontab file `(sudo crontab -e)` to reflect Test or Production
* Delete the data out of the production db.  Change directory to Prod then type `sqlite3`, then type `.open prod_records.db`, then type `DELETE FROM TRANSX`
* Delete the ODTS-mini-Scan-old folder:  `sudo rm -r ODTS-mini-Scan-old`
* Scet the barcode scanner to Auto Continuous Mode by scanning a code in the manual.
* Adjust the contrast on the LCD display.
* Remove the usb adapters for the keyboard and mouse.
* Screw the lid back on.
* Disconnect the monitor and reboot the Pi.  The new box should now perform like other production boxes.
* All of the production boxes (remotes) will pull the repo on a daily basis.
  
 
