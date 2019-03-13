import math 
import os 
from PIL import Image, ImageColor, ImageDraw, ImagePath
from os import path


path = "pics_pngs"

if not os.path.exists(path):
    os.mkdir("pics_pngs")


def one_color():
    pic = Image.new('RGB', (50, 50), color = 'cyan')
    pic.save('monocolor.png')


def colorful():
    pic = Image.new('RGB', (300, 300), color = 'blue')
    x, y = pic.size
    eX, eY = 60, 60 

    pic_in =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
    draw = ImageDraw.Draw(pic)
    draw.ellipse(pic_in, fill='green', outline='white')
    draw.line((0,0, 300,300), fill='red', width=3)
    draw.line((0,30, 300, 270), fill='red', width=2)
    draw.line((0,60, 300, 240), fill='red', width=1)
    
    xy = [
    (i, (math.sin(i / 64. * math.pi) + 1) * 150)
    for i in range(300)
    ]

    bbox = ImagePath.Path(xy).getbbox()
    size = list(map(int, map(math.ceil, bbox[2:])))
    
    draw.point(xy, fill='yellow')

    x_y = [
    (i, (math.cos(i / 64. * math.pi) + 1) * 150)
    for i in range(300)
    ]

    bbox = ImagePath.Path(xy).getbbox()
    size = list(map(int, map(math.ceil, bbox[2:])))
    
    draw.point(x_y, fill='yellow')

    xxy = [
    (i, (math.tan(i / 64. * math.pi) + 1) * 150)
    for i in range(300)
    ]

    bbox = ImagePath.Path(xy).getbbox()
    size = list(map(int, map(math.ceil, bbox[2:])))
    
    draw.point(xxy, fill='yellow')
    
    draw.arc((0,0, 300,300), start= 300, end= 30, fill='pink')
    draw.arc((0,0, 300,300), start= 30, end= 300, fill='pink')
    
    del draw
    fullpath = (os.path.join(path, "duo.png"))
    pic.save(fullpath)
    pic.show()


if __name__ == "__main__":
    # one_color()
    colorful()