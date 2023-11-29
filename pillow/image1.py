from PIL import Image

image_file = "casa.jpg"
im = Image.open(image_file)
im.show()
imim = im.rotate(45)
imim.show()
