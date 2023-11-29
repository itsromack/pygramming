from PIL import Image

def thumbnailer():
    try:
        image_file = "casa.jpg"
        im = Image.open(image_file)
        im.thumbnail((80, 80))

        image_thumbnail_file = "image_thumbnail.jpg"
        # Save Thumbnail file
        im.save(image_thumbnail_file)

        thumb = Image.open(image_thumbnail_file)
        thumb.show()
    except IOError:
        print("An error occured")


thumbnailer()
