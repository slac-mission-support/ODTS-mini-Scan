# Description

Decode nearly any kind of 1D (striped) barcode in your project using this adorable compact barcode scanner. We've looked all over for a small, light, low-power module that can be easily integrated. This OEM scanner has a little camera inside that takes 100 photos per second, instead of using a 'scanning mirror' assembly. This means its less likely to get damaged or out of alignment. 

Please note: this is a camera-based not laser-based scanner - you'll have to hold it farther away than you usually do for laser-mirror scanners! Try 10cm/4" or more distance with the button held down.

This all in one module is the simplest we could find. On the end is just a USB cable, plug it into any computer (or microcomputer such as BeagleBone, Raspberry Pi, etc) and it will show up as an HID keyboard. When a barcode is scanned, the raw data is decoded, parity-checked and spit out as if they were typed on a keyboard.

Like all barcode scanners, you can do some basic configuration by powering it up and 'scanning' in special barcodes in the manual. For example you can change the delay between 'typed' characters, or what the terminating character, if any, should be. Check the download tab for the printable manual. If you'd like to set up the scanner to be different than the default, print it out on plain white paper and scan each 'configuration' code. The config will be saved to non-volatile memory so you only have to do it once.

This reader will read a wide variety of barcode standards. The most common ones such as CODE39 and UPC are supported out of the box. To enable some of the rarer standards, check the manual as you may have to 'scan configure' to enable it.
