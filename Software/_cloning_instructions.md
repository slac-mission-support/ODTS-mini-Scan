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
* Delete the ODTS-mini-Scan folder in `/home/ryanford`, then re-clone it to create a unique remote
  * `cd /home/ryanford`
  * `git clone https://github.com/ryanfordSLAC/ODTS-mini-Scan.git`
* Revise config.py in the Prod folder of ODTS-mini-Scan to reflect the new hostname.
* Revise config.py to reflect the event file in /dev/input which receives data from the barcode scanner.
  * To determine which event file captures the scanner input, type `cat /proc/bus/input/devices` at a command prompt
* Execute the config.py file to create config.ini.
* Edit the rc.local file (sudo nano /etc/rc.local) and uncomment the line which runs Capture_barcode.py on boot.  This line should be enabled when the box is run headless (without monitor).
* Disconnect the monitor and reboot the Pi.  The new box should now perform like other production boxes.
* All of the production boxes (remotes) will pull the repo on a daily basis.
  
 
