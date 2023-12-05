# Libraries

## email library (email_class.py)
Connects to an smtp server and sends an email
- email.send_email(slac_ID, name, recipients, return_date, period_code, dosimeter_number, body_option)

## fetch data library (ODTS.py)
Contains sql commands and connection information to connect to ODTS.
- odts.fetch_data_using_dosinumber()
- odts.update_ODTS_return_date()

## tally scans library (sqlite_tally.py)
Contains sql commands and connection information to write successful scan metadata into a SQLite DB on localhost.
- tally_sqlite.update_SQLlite_tally()

## rgb light library (class_rgb.py)
Controls the RGB LED light (common anode type), connected to pi on 4 pins.  Note flashing state flashes 10 times at 0.2 seconds per flash.
- LED.red(state), where state 1 is steady light, and state 2 is flashing
- LED.blue(state), where state 1 is steady light, and state 2 is flashing
- LED.green(state), where state 1 is steady light, and state 2 is flashing
- LED.yellow(state), where state 1 is steady light, and state 2 is flashing
- LED.purple(state), where state 1 is steady light, and state 2 is flashing
- LED.lightBlue(state), where state 1 is steady light, and state 2 is flashing
- LED.white(state), where state 1 is steady light, and state 2 is flashing
- LED.turnOff(state), where state 1 is steady light


## 2 x 16 LCD Display Default Message Library (LCD_messages.py)
Contains standard messages shown in the software specification
- messages.message1(), no arguments
- messages.message2(dosinumber)
- messages.message3(), no arguments
- messages.message4(), no arguments
- messages.message5(), no arguments
- messages.message6a(lastname, firstname)
- messages.message6b(returndate)
- messages.message7(), no arguments
- messages.message8(), no arguments
- messages.message9(), no arguments

## I2C Library (I2C_LCD_driver.py)
Library taken from internet 
- lcd.backlight(state), where option 1 is on, and option 2 is off
- lcd.lcd_display_string(string, line, position), where line = 1 or 2, and position is 1 - 16.
- lcd.lcd_clear()
- additional unused functions

