from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')
imgFilter = img.convert('L')
imgFilter.save("L.png", 'png')
