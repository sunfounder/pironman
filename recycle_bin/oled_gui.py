from time import sleep
from oled import SSD1306_128_64
from PIL import Image,ImageFont,ImageDraw


# 128x64 display with hardware I2C:
disp = SSD1306_128_64()

# Get display width and height.
width = disp.width
height = disp.height

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()
sleep(0.01)

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as this python script!
# Some nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)


# Define text and get total width.
text = 'Hello !!!'
maxwidth, unused = draw.textsize(text, font=font)

startpos = width
velocity = -2
pos = startpos

def fuc():
    # Clear image buffer by drawing a black filled box.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    x = 0
    for i, c in enumerate(text):
        char_width, char_height = draw.textsize(c, font=font)
        x += char_width
           
        y = 12
        print(i)
        # Draw text.
        draw.text((x, y), c, font=font, fill=255)
        # Increment x position based on chacacter width.
        # char_width, char_height = draw.textsize(c, font=font)
        # x += char_width
    # Draw the image buffer.
    disp.image(image)
    disp.display()
        # Move position for next frame.
    pos += velocity
    # Start over if text has scrolled completely off left side of screen.
    if pos < -maxwidth:
        pos = startpos

    # Pause briefly before drawing next frame.
    sleep(0.1)


if __name__ == "__main__":
    # fuc()
    fuc('hello')

