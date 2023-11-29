from PIL import Image, ImageFilter

image_file = "lighthouse.jpg"
im = Image.open(image_file)
im.show()

blur = im.filter(ImageFilter.BLUR)
blur.show()

box_blur = im.filter(ImageFilter.BoxBlur(radius=1))
box_blur.show()

gblur = im.filter(ImageFilter.GaussianBlur(radius=2))
gblur.show()
