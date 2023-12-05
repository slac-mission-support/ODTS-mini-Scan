# Libraries

## email library
Connects to an smtp server and sends an email
- email.send_email(1, 2, 3, 4, 5, 6, 7)

## fetch data library
Contains sql commands and connection information to connect to ODTS.
- odts.fetch_data_using_dosinumber()
- odts.update_ODTS_return_date()

## tally scans library
Contains sql commands and connection information to write successful scan metadata into a SQLite DB on localhost.
- tally_sqlite.update_SQLlite_tally()

## rgb light library
Controls the RGB LED light (common anode type), connected to pi on 4 pins.  Note flashing option flashes 10 times at 0.2 seconds per flash.
- LED.red(option), where option 1 is steady light, and option 2 is flashing
- LED.blue(option), where option 1 is steady light, and option 2 is flashing
- LED.green(option), where option 1 is steady light, and option 2 is flashing
- LED.yellow(option), where option 1 is steady light, and option 2 is flashing
- LED.purple(option), where option 1 is steady light, and option 2 is flashing
- LED.lightBlue(option), where option 1 is steady light, and option 2 is flashing
- LED.white(option), where option 1 is steady light, and option 2 is flashing
- LED.turnOff(option), where option 1 is steady light, and option 2 is flashing


## 16 x 2 LCD Display Default Message Library
Contains standard messages shown in the software specification
- LCD.message(message_number), where message_numbers 1 - 10 represent the messages in the specification.

## I2C Library
Library taken from internet 
- I2C.backlight(option), where option 1 is on, and option 2 is off
- I2C.write_message()

