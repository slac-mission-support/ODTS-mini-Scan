# ODTS-mini-Scan
Created November, 2023

The purpose of the mini-Scan is to enable users of the personal dosimeter service to register dosimeter returns directly into ODTS and receive an email confirmation.  This transaction is intended to reduce or eliminate cases where the user states they've returned it, but the dosimetry group hasn't received it.  More importantly, the transaction supplies written proof of the return via email.

## Hardware

Hardware consists of the following:
* Raspberry Pi version 4
* Adafruit USB barcode scanner
* 2 x 16 character LCD display using I2C protocol
* RGD Led diode
* Terminal block breakout board for Raspberry Pi (optional)
* 90 degree USB connector
* 6 x 4 x 2" project box with clear lid
* USB-C charger/power supply
* Custom mounting board
* 2.0 mm, 2.5 mm, 3.0 mm standoff kit
* 22 AWG wiring kit

## Software

Software is in the form of python scripts used to control the GPIO, and to connect and make transactions into the ODTS database.  The python file is intended to reside in the rc.local file where it will run on boot and continuously thereafter (Edit the file using the following terminal command: sudo nano /etc/rc.local).  The software specification (for the python script) is outlined in the attached Word document.

* I2C Library File
* Python script
* Software specification (Word file)
