from PIL import Image, ImageColor, ImageDraw

pic = Image.new('RGB', (50, 50), color = 'cyan')
pic.save('monocolor.png')