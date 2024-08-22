import hid

for device_dict in hid.enumerate():
    keys = list(device_dict.keys())
    keys.sort()
    for key in keys:
        print("%s : %s" % (key, device_dict[key]))
    print()

#device is 0483, 0011 HEX
#device is 1155, 17 DEC


