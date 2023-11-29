from PIL import Image

image_file = "casa.jpg"
im = Image.open(image_file)
print("Filename ", im.filename)
print("Format", im.format)
print("Mode", im.mode)
print("Size", im.size)
print("Width", im.width)
print("Height", im.height)
print("Info", im.info)
