from PIL import Image

image_file = "casawater.jpg"
im = Image.open(image_file)
im.show()

hflip = im.transpose(Image.FLIP_LEFT_RIGHT)
hflip.show()

vflip = im.transpose(Image.FLIP_TOP_BOTTOM)
vflip.show()
