import I2C_LCD_driver

    
mylcd = I2C_LCD_driver.lcd()

class messages():

    def message1(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("READY", 1,0)
        mylcd.lcd_display_string("TO SCAN...", 2,0)
        
    def message2(self, dosinumber):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string(dosinumber, 1,0)
        mylcd.lcd_display_string("SEARCHING...", 2,0)
        
    def message3(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("CONNECTED...", 1,0)

    def message4(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("RECORD FOUND...", 1,0)

    def message5(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("RETURN", 1,0)
        mylcd.lcd_display_string("SUCCESSFUL!", 2,0)
        
    def message6a(self, lastname, firstname):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string(lastname, 1,0)
        mylcd.lcd_display_string(firstname, 2,0)
        
    def message6b(self, returndate):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("RETURNED ON", 1,0)
        mylcd.lcd_display_string(returndate, 2,0)
        
    def message7(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("UNKNOWN DOSI", 1,0)
        mylcd.lcd_display_string("PLEASE TRY AGAIN!", 2,0)
        
    def message8(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("NETWORK", 1,0)
        mylcd.lcd_display_string("FAILURE!", 2,0)
        
    def message9(self):
        
        mylcd.lcd_clear()
        mylcd.lcd_display_string("CONFIRMATION", 1,0)
        mylcd.lcd_display_string("SENT VIA EMAIL", 2,0)

