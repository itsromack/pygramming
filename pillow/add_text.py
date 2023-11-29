# You might encounter an error on missing textsize() method
# 
# install Pillow with this version
# python -m pip install Pillow==9.5.0
#
from PIL import Image, ImageDraw

image_file = "5f.jpg"
im = Image.open(image_file)
w, h = im.size

draw = ImageDraw.Draw(im)

text1 = 'THE FIVE FINGERS - CSM Bataan Python Programmers'
text1_color = (255, 255, 0)
text1_coordinates = (400, 500)

# Add text
draw.text(text1_coordinates, text1, text1_color)
im.show()
