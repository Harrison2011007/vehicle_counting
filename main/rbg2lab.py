from PIL import Image

imTree = Image.open('D:\\Program Files (x86)\\vehicle_counting\\1.jpg')
pix = imTree.load()
Twidth = imTree.size[0]
Theight = imTree.size[1]
# print(Twidth)
imTree = imTree.convert('RGB')
rgbarray = []

for x in range(Twidth):
    for y in range(Theight):
        r, g, b = imTree.getpixel((x, y))
        rgb = r, g, b
        rgbarray.append(rgb)
print(rgbarray[0])
print(rgbarray[0][0])
l = []
l = 0.2126007 * rgbarray[0][0] + 0.7151947 * rgbarray[0][1] + 0.0722046 * rgbarray[0][2]
a = 0.3258962 * rgbarray[0][0] - 0.4992596 * rgbarray[0][1] + 0.1733409 * rgbarray[0][2] + 128
b = 0.1218128 * rgbarray[0][0] + 0.3785610 * rgbarray[0][1] - 0.5003738 * rgbarray[0][2] + 128
l = int(l)
a = int(a)
b = int(b)

print(l)
print(a)
print(b)
