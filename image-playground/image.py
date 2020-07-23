from PIL import Image, ImageFilter

#this will create another image and blur it
img = Image.open("./models/model1.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", "png")

img2 = Image.open("./models/model2.jpg")
filtered_img2 = img2.filter(ImageFilter.SMOOTH)
filtered_img2.save("smooth.png", "png")

img3 = Image.open("./models/model3.jpg")
filtered_img3 = img3.convert('L')
filtered_img3.save("grey.png", "png")
filtered_img3.show()
crooked = filtered_img3.rotate(90)
crooked.save("grey.png", "png")

resize = filtered_img3.resize((300,300))
resize.save("grey.png", "png")


box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", "png")

img = Image.open("./earth.jpg")
img.thumbnail((400,400))
img.save("thumbnail.jpg")