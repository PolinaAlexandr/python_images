import math 
import os 
# import random
from PIL import Image, ImageColor, ImageDraw, ImagePath
from os import path

path = "pics_pngs"

if not os.path.exists(path):
    os.mkdir("pics_pngs")

xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5 
maxIt = 256
picx = 1024
picy = 768

pic = Image.new("RGB", (picx, picy))
# draw = ImageDraw.Draw(pic)

for y in range(picy):
    cy = y * (yb - ya) / (picy - 1) + ya
    for x in range(picx):
        cx = x * (xb - xa) / (picx - 1) + xa
        c = complex(cx, cy)
        z = 0 

        for i in range(maxIt):
            if abs(z) > 2.0:
                break
            z = z * z + c 
        r = i % 4 * 8 
        g = i % 8 * 32 
        b = i % 16 * 128 

        pic.putpixel((x, y), b * 65536 + g * 256 + r)

fullpath = (os.path.join(path, "mandelbrot_fractal.png"))
pic.save(fullpath)
pic.show()