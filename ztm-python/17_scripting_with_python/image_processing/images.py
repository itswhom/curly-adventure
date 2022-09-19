from PIL import Image, ImageFilter

# load up an image, filter to be b&w then rotate 90deg
# img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# crooked.save('rotated.png', 'png')

# resize the image to be smaller
# resized = filtered_img.resize((300,300))
# resized.save('thumb.png','png')
# # resized.show()

# crop to a region of the image
# box = (100,100,400,400)
# region = filtered_img.crop(box)
# region.save('crop-in.png','png')

img = Image.open('./astro.jpg')
img.thumbnail((400,400))
img.save('thumbnail.jpg')