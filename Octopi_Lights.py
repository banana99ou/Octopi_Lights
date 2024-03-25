import time
import board
import neopixel
import sys


pixel_pin = board.D18

num_pixels = 40
R = 0
G = 0
B = 0

if len(sys.argv) > 1:
   R = int(sys.argv[1])
else:
   R = 0
if len(sys.argv) > 2:
   G = int(sys.argv[2])
else:
   G = 0
if len(sys.argv) > 3:
   B = int(sys.argv[3])
else:
   B = 0


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

pixels.fill((255, 255, 255))
pixels.show()