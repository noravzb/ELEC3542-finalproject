from sense_hat import SenseHat
import time
import numled

sense = SenseHat()
colors = [(255, 0, 0), (255, 255, 255)]

for i in range(0, 10):
	numled.show_number(sense, i, colors[i % len(colors)])
	time.sleep(1)
