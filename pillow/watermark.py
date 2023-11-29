# You might encounter an error on missing textsize() method
# 
# install Pillow with this version
# python -m pip install Pillow==9.5.0
#
from PIL import Image, ImageDraw, ImageFont

image_file = "lighthouse.jpg"
im = Image.open(image_file)
w, h = im.size

draw = ImageDraw.Draw(im)

text1 = 'THE LIGHTHOUSE'

# Specify font family and size
font = ImageFont.truetype('arial.ttf', 24)
textw, texth = draw.textsize(text1, font=font)

# calculate coordinates
margin = 10
x = w - textw - margin
y = h - texth - margin

# draw watermark
draw.text((x, y), text1, font=font)
im.show()
