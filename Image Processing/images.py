from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')

print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')


astro_img = Image.open('./astro.jpg')
print(astro_img.size)
astro_img.thumbnail((400, 400))
astro_img.save('thumbnail.jpg')
print(astro_img.size)
