import font8x8 as font

def show_number(sense, value, color=(255, 255, 255)):
	"""
	Displays the specified two-digit integer on the LED matrix of Sense HAT.
	
	Parameters
	----------
	sense : SenseHat
		The Sense HAT instance being used.
	value : int
		An integer between 0 and 99.
	color : (int, int, int)
		A tuple or list representing the RGB color of the digit's display 
		color. Each element must be an integer between 0 and 255. The default
		value is (255, 255, 255).
	"""
	if value < 0 or value > 12:
		raise ValueError("value must be in the range of 0 to 12")
	sense.clear()
	show_digit(sense, value, color=color)

def show_digit(sense, value, x=0, y=0, color=(255, 255, 255)):
	"""
	Displays the specified digit on the given position of the LED matrix of 
	Sense HAT.
	
	Parameters
	----------
	sense : SenseHat
		The Sense HAT instance being used.
	value : int
		An integer between 0 and 9.
	x : int
		The x-coordinate of the top-left anchor point of the digit. 0 is on 
		the left, 7 on the right. The default value is 0.
	y: int
		The y-coordinate of the top-left anchor point of the digit. 0 is at 
		the top, 7 at the bottom. The default value is 0.
	color : (int, int, int)
		A tuple or list representing the RGB color of the digit's display 
		color. Each element must be an integer between 0 and 255. The default
		value is (255, 255, 255).
	"""
	if not sense:
		raise Exception("Sense HAT is unavailable")
	if value < 0 or value > 12:
		raise ValueError("value must be in the range of 0 to 12")
	digit = font.digits[value]
	for column in range(x, x + font.width):
		for row in range(y, y + font.height):
			if digit[(row - y) * font.width + (column - x)] == 0:
				sense.set_pixel(column, row, (0, 0, 0))
			else:
				sense.set_pixel(column, row, color)
