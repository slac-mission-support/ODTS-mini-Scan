# ODTS-mini-Scan
Created November, 2023

The purpose of the mini-Scan is to enable users of the personal dosimeter service to register dosimeter returns directly into ODTS and receive an email confirmation.  This transaction is intended to reduce or eliminate cases where the user states they've returned it, but the dosimetry group hasn't received it.  Furthermore, the transaction supplies written proof of the return via email.

Most importantly, the mini-Scan replaces the time-consuming process of using the "Return Dosimeters" utility in ODTS with a single scan on the device.

## Hardware

Preferably the device connects to the SLAC network via WiFi; however if this is not possible the pi has an ethernet port.  If only the power cable is needed then the devices can be attached to the wall next to the dosimeter racks, which will enable us to place more scanners in the field.

Hardware consists of the following:
* Raspberry Pi version 4
* Adafruit USB barcode scanner
* 2 x 16 character LCD display using I2C protocol
* RGB Led diode
* Terminal block breakout board for Raspberry Pi (optional)
* 90 degree USB connector (optional)
* Project box for tabletop or wall mount
* USB-C charger/power supply
* Custom mounting board
* 2.0 mm, 2.5 mm, 3.0 mm standoff kit
* 22 AWG wiring kit
* Momentary push button (pre-wired)

![Pi](https://github.com/ryanfordSLAC/ODTS-mini-Scan/blob/main/Photos/Device-2.jpg)
## Software (onboard)

Software is in the form of python scripts used to control the GPIO, and to connect and make transactions into the ODTS database.  The python file is intended to reside in the rc.local file where it will run on boot and continuously thereafter (Edit the file using the following terminal command: sudo nano /etc/rc.local).  The software specification (for the python script) is outlined in the attached Word document.

* Library Files (see Overview.md)
* Python script
* Software specification (file) Word file)

## Software (web)
* System Health viewer (see Word file)
