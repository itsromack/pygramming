from PIL import Image, ImageFilter
from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)

image_file = "bean.png"
im = Image.open(image_file)
im.show()

filtered = im.filter(BLUR)
filtered.show()

filtered = im.filter(CONTOUR)
filtered.show()

filtered = im.filter(DETAIL)
filtered.show()

filtered = im.filter(EDGE_ENHANCE)
filtered.show()

filtered = im.filter(EDGE_ENHANCE_MORE)
filtered.show()

filtered = im.filter(EMBOSS)
filtered.show()

filtered = im.filter(FIND_EDGES)
filtered.show()

filtered = im.filter(SMOOTH)
filtered.show()

filtered = im.filter(SMOOTH_MORE)
filtered.show()

filtered = im.filter(SHARPEN)
filtered.show()

