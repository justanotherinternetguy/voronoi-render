from PIL import Image
import random
import math

def generate_euclid(w, h, num_cells):
	img = Image.new("RGB", (w, h))
	putpixel = img.putpixel
	img_x, img_y = img.size
	
	nx = []
	ny = []
	nr = []
	ng = []
	nb = []
	
	for i in range(num_cells):
		nx.append(random.randrange(img_x))
		ny.append(random.randrange(img_y))
		nr.append(random.randrange(256))
		ng.append(random.randrange(256))
		nb.append(random.randrange(256))

	for y in range(img_y):
		for x in range(img_x):
			dmin = math.hypot(img_x-1, img_y-1)
			j = -1
			for i in range(num_cells):
				d = math.hypot(nx[i]-x, ny[i]-y)
				if d < dmin:
					dmin = d
					j = i
			putpixel((x, y), (nr[j], ng[j], nb[j]))
	img.save("test.png", "PNG")
	img.show()

generate_euclid(500, 500, 10)
