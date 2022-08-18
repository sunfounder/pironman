import time
import random
from rpi_ws281x import Adafruit_NeoPixel, Color
from utils import log

# LED strip configuration:
# LED_COUNT      = 8      # Number of LED pixels.
# LED_PIN        = 12      # GPIO pin connected to the pixels (must support PWM!).
# LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA        = 10       # DMA channel to use for generating signal (try 5)
# LED_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
# LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


RGB_styles = ['breath', 'leap', 'flow', 'raise_up']

class WS2812():

	lights_order = [1, 3, 5, 7, 0, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15]

	def __init__(self,
				LED_COUNT,
				LED_PIN, 
				LED_BRIGHTNESS=255,
				LED_FREQ_HZ=800000, 
				LED_DMA=10, 
				LED_INVERT=False, 
				):
		self.led_count = LED_COUNT
		self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
		self.strip.begin()


	# eg: 'ffffff', '#ffffff', '#FFFFFF'
	def Hex_to_RGB(self, hex:str):
		try:
			hex = hex.strip().replace('#','')
			r = int(hex[0:2], 16)
			g = int(hex[2:4], 16)
			b = int(hex[4:6], 16)
			return [r, g, b]
		except Exception as e:
			log('color parameter error: \n%s'%e)


	def clear(self, color:str='#000000'):
		r, g, b = self.Hex_to_RGB(color)
		self.strip.begin()
		for i in range(self.led_count):
			self.strip.setPixelColor(i, Color(r,g,b))
		self.strip.show() 


	def display(self, style:str, color:str, speed=50, brightness=255):
		color = list(self.Hex_to_RGB(color))
		self.clear()
		self.strip.begin()
		# eval is evil, list The list is split into individual characters
		# eval('self.%s(color="%s", speed=%s)'%(style, color, speed))
		try: 
			# globals()[style](color, speed)
			fuc = getattr(self,style)
			fuc(color, speed)
		except KeyError:
			log('LED strip parameter error: [style]')


# styles
	def breath(self, color:list=[255, 255, 255], speed=50):	
		speed = 101 - speed
		self.strip.begin()
		while True:
			for i in range(2,101):
				r, g, b = [int(x*i*0.01) for x in color]
				# print('%s: %s, %s, %s'%(i,r,g,b))
				for index in self.lights_order:
					self.strip.setPixelColor(index, Color(r,g,b))	
				self.strip.show()
				time.sleep(0.001*speed)
			for i in range(100,1,-1): 
				r, g, b = [int(x*i*0.01) for x in color]
				for index in self.lights_order:
					self.strip.setPixelColor(index, Color(r,g,b))	
				self.strip.show()
				time.sleep(0.001*speed) 
			
			# r,g,b = color
			# for index in self.lights_order:
			# 	self.strip.setPixelColor(index, Color(r,g,b))	
			# self.strip.show()	
			# time.sleep(0.001*speed)		
	
	
	def leap(self, color:list=[255, 255, 255], speed=50):
		self.strip.begin()
		speed = 101 - speed
		r,g,b = color
		while True:
			for i in range(self.led_count):
				for index in self.lights_order:
					self.strip.setPixelColor(index, Color(0,0,0))
				self.strip.setPixelColor(i, Color(r,g,b))
				self.strip.show()
				time.sleep(0.001*speed)


	def flow(self, color:list=[255, 255, 255], speed=50):
		self.strip.begin()
		speed = 101 - speed
		r,g,b = color
		while True:
			for index in self.lights_order:
				self.strip.setPixelColor(index, Color(r,g,b))
				self.strip.show()
				time.sleep(0.001*speed)
			for j in range(self.led_count):
				self.strip.setPixelColor(j, Color(0,0,0))
			self.strip.show()
			time.sleep(0.005*speed)


	def raise_up(self, color:list=[255, 255, 255], speed=50):
		self.strip.begin()
		speed = 101 - speed
		r,g,b = color
		while True:
			for i in range(2,101):
				r, g, b = [int(x*i*0.01) for x in color]
				for index in range(0, 4, 1):
					self.strip.setPixelColor(self.lights_order[index], Color(r,g,b))
				self.strip.show()
				time.sleep(0.0002*speed)
			for i in range(2,101):
				r, g, b = [int(x*i*0.01) for x in color]
				for index in range(4, 8, 1):
					self.strip.setPixelColor(self.lights_order[index], Color(r,g,b))
				self.strip.show()
				time.sleep(0.0002*speed)
			for i in range(2,101):
				r, g, b = [int(x*i*0.01) for x in color]
				for index in range(8, 16, 1):
					self.strip.setPixelColor(self.lights_order[index], Color(r,g,b))
				self.strip.show()
				time.sleep(0.0002*speed)
			# turn off
			time.sleep(10*0.0005*speed)
			for index in self.lights_order:
				self.strip.setPixelColor(self.lights_order[index], Color(0,0,0))
				self.strip.show()
				time.sleep(0.001*speed)


if __name__ == "__main__":
	speed = 50
	strip = WS2812(16, 12)
	# strip.display('breath','#0000ff', speed=speed)
	strip.display(style='leap',color='#0000ff', speed=speed)
	# strip.display(style='flow',color='#1a1aff', speed=speed)
	# strip.display(style='raise_up',color='#1a1aff', speed=speed)




