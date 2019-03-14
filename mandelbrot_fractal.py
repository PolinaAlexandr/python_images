import math 
import os 
from PIL import Image, ImageColor, ImageDraw, ImagePath
from os import path

path = "pics_pngs"

if not os.path.exists(path):
    os.mkdir("pics_pngs")
