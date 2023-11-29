from PIL import Image

image_file = "spidey.png"
im = Image.open(image_file)
im.show()

flip90 = im.transpose(Image.ROTATE_90)
flip90.show()

flip180 = flip90.transpose(Image.ROTATE_90)
flip180.show()

flip270 = flip180.transpose(Image.ROTATE_90)
flip270.show()

im.show()
