import hid

try:
    print("Opening the device")

    h = hid.device()
    h.open(0x0483, 0x0011)  # Barcode Scanner
    #h.open(0,0)
    #h.open(0x413C, 0x301D) #Dell
    
    
    print("Manufacturer: %s" % h.get_manufacturer_string())
    print("Product: %s" % h.get_product_string())
    print("Serial No: %s" % h.get_serial_number_string())

    # enable non-blocking mode
    h.set_nonblocking(1)

    # write some data to the device
    print("Write the data")
    h.write([0, 63, 35, 35] + [0] * 61)

    # wait
    time.sleep(0.05)

    # read back the answer
    print("Read the data")
    while True:
        d = h.read(64)
        if d:
            print(d)
        else:
            break

    print("Closing the device")
    h.close()

except IOError as ex:
    print(ex)
    print("You probably don't have the hard-coded device.")
    print("Update the h.open() line in this script with the one")
    print("from the enumeration list output above and try again.")

print("Done")