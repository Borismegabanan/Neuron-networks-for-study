from PIL import Image, ImageDraw
img = Image.open("photo.jpg")
draw=ImageDraw.Draw(img)

width=img.size[0]
height=img.size[1]
pix=img.load()

i=0

for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))
            
img.save("ans.jpg", "JPEG")
del draw

