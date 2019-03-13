from PIL import Image, ImageColor, ImageDraw
import os 
from os import path


path = "pics_pngs"

if not os.path.exists(path):
    os.mkdir("pics_pngs")


def one_color():
    pic = Image.new('RGB', (50, 50), color = 'cyan')
    pic.save('monocolor.png')


def color_duo():
    pic = Image.new('RGB', (300, 300), color = 'blue')
    x, y = pic.size
    eX, eY = 60, 50 

    pic_in =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
    draw = ImageDraw.Draw(pic)
    draw.ellipse(pic_in, fill='green', outline='white')

    del draw
    fullpath = (os.path.join(path, "duo.png"))
    pic.save(fullpath)
    pic.show()


if __name__ == "__main__":
    # one_color()
    color_duo()