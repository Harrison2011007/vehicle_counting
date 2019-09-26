from PIL import Image


imTree = Image.open('E:\\work2019\\Mar\\images\\car.jpg')
pix = imTree.load()
Twidth = imTree.size[0]
Theight = imTree.size[1]
print(Twidth)
imTree = imTree.convert('RGB')
rgbarray = []

for x in range(Twidth):
    for y in range(Theight):
        r,g,b = imTree.getpixel((x,y))
        rgb = r,g,b
        rgbarray.append(rgb)
print(rgbarray[0])
print(rgbarray[0][0])
l = []
l = 0.2126007 * rgbarray[0][0] + 0.7151947 * rgbarray[0][1] + 0.0722046 * rgbarray[0][2]
print(l)