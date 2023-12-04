# Libraries

## email library
Connects to an smtp server and sends an email
-send_email(1, 2, 3, 4, 5, 6, 7)

## fetch data library
Contains sql commands and connection information to connect to ODTS.
- fetch_data_using_dosinumber()
- update_ODTS_return_date()

## tally scans library
Contains sql commands and connection information to write successful scan metadata into a SQLite DB on localhost.
-update_SQLlite_tally()

## rgb light library
- red(option), where ooption 1 is steady light, and option 2 is flashing
- blue(option), where ooption 1 is steady light, and option 2 is flashing
- green(option), where ooption 1 is steady light, and option 2 is flashing
- yellow(option), where ooption 1 is steady light, and option 2 is flashing
- purple(option), where ooption 1 is steady light, and option 2 is flashing
- lightBlue(option), where ooption 1 is steady light, and option 2 is flashing
- white(option), where ooption 1 is steady light, and option 2 is flashing
- turnOff(option), where ooption 1 is steady light, and option 2 is flashing


## 16 x 2 LCD Display Default Message Library
Contains standard messages shown in the software specification
-message(message_number), where message_numbers 1 - 10 represent the messages in the specification.

## I2C Library
Library taken from internet 
-backlight(option), where option 1 is on, and option 2 is off
-write_message()

