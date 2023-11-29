from PIL import Image, ImageOps

image_file = "bean.png"
im = Image.open(image_file)
imb = ImageOps.expand(im, border=70, fill='pink')
imb.show()
