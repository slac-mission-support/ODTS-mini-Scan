from evdev import InputDevice, categorize, ecodes
dev = InputDevice('/dev/input/event13')
for event in dev.read_loop():
		if event.type == ecodes.EV_KEY:
				print(categorize(event))



