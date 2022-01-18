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


class WS2812():
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
				print('%s: %s, %s, %s'%(i,r,g,b))
				for j in range(self.led_count):
					self.strip.setPixelColor(j, Color(r,g,b))	
				self.strip.show()
				time.sleep(0.001*speed)
			for i in range(100,1,-1):
				r, g, b = [int(x*i*0.01) for x in color]
				for j in range(self.led_count):
					self.strip.setPixelColor(j, Color(r,g,b))	
				self.strip.show()
				time.sleep(0.001*speed)  
	
	
	def flow(self, color:list=[255, 255, 255], speed=50):
		self.strip.begin()
		speed = 101 - speed
		r,g,b = color
		while True:
			for i in range(self.led_count):
				for j in range(self.led_count):
					self.strip.setPixelColor(j, Color(0,0,0))
				self.strip.setPixelColor(i, Color(r,g,b))
				self.strip.show()
				time.sleep(0.003*speed)


if __name__ == "__main__":

	strip = WS2812(16, 12)
	strip.display('breath','#0000ff', speed=50)
	# strip.display(style='flow',color='#0000ff', speed=10)


