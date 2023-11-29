from PIL import Image

image_file = "bean.png"
im = Image.open(image_file)
im.show()

width, height = im.size

left = 5
top = height / 4
right = 200
bottom = 3 * height / 4

cropped = im.crop((left, top, right, bottom))
cropped.show()
