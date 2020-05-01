
import time
import subprocess

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white filled box to clear the image.
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

# Load default font.
#font = ImageFont.load_default()

# Alternatively load a TTF font.
# Some nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('/home/pi/04B_03__.TTF', 8)

cmd = "hostname"
HOSTNAME = subprocess.check_output(cmd, shell=True).decode("utf-8").rstrip()

cmd = "hostname -I"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8").rstrip()
cmd = "date +\"%b %d, %Y\""
DATE = subprocess.check_output(cmd, shell=True).decode("utf-8").rstrip()
cmd = "uptime | awk -F'up' '{print $2}' | awk -F',' '{print $1}'"
#cmd = "uptime | awk '{print $3 $4}' | tr -d \",\""
UPTIME = subprocess.check_output(cmd, shell=True).decode("utf-8").rstrip().lstrip()

#print IP
#print DATE
#print UPTIME.lstrip()

# Write some text.
draw.text((0,10), 'IP: '+IP, font=font)
draw.text((0,20), 'Uptime: ', font=font)
draw.text((34,20), UPTIME, font=font)
draw.text((0,30), 'Date: '+DATE, font=font)
draw.text((0,0), HOSTNAME, font=font)
draw.text((0,40), 'Bottom', font=font)

# Display image.
disp.image(image)
disp.display()

#print('Press Ctrl-C to quit.')
#while True:
#    time.sleep(1.0)
