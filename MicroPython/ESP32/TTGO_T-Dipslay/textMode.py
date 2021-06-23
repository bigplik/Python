"""
text
    mode

"""

import random
from machine import Pin, SoftSPI
import st7789py as st7789

# Choose a font

# from romfonts import vga1_8x8 as font
# from romfonts import vga2_8x8 as font
# from romfonts import vga1_8x16 as font
# from romfonts import vga2_8x16 as font
# from romfonts import vga1_16x16 as font
# from romfonts import vga1_bold_16x16 as font
# from romfonts import vga2_16x16 as font
import vga2_bold_16x16 as font
# from romfonts import vga1_16x32 as font
# from romfonts import vga1_bold_16x32 as font
# from romfonts import vga2_16x32 as font
#from romfonts import vga2_bold_16x32 as font

def main():
    spi = SoftSPI(
        baudrate=20000000,
        polarity=1,
        phase=0,
        sck=Pin(18),
        mosi=Pin(19),
        miso=Pin(13))

    tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(23, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=0)
    
    tft.fill(st7789.CYAN)
    
    while True:
        tft.rotation(3)
        #                           W   H  font color    background color
        tft.text(font, "text mode", 50, 20, st7789.WHITE, st7789.BLACK)

main()