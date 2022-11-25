from PIL import Image, ImageDraw
import random
import math

class Seed():
    def __init__(self, r, g, b, x, y, draw, putpixel):
        self.r = r
        self.g = g
        self.b = b
        self.x = x
        self.y = y
        self.draw = draw
        self.putpixel = putpixel
        
    def euclideanDistance(self, x1, y1, x2, y2):
        return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    def setColor(self):
        self.r = random.randint(1, 255)
        self.g = random.randint(1, 255)
        self.b = random.randint(1, 255)

    def setLocation(self, w, h):
        self.x = random.randint(0, w)
        self.y = random.randint(0, h)

    def getColor(self):
        return (self.r, self.g, self.b)

    def getLocation(self):
        return (self.x, self.y)

    def drawCenter(self):
        self.draw.rectangle([(self.x-5, self.y-5), (self.x+5, self.y+5)], fill=(255, 255, 255))


def generate_euclid(w, h, num_seeds):
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    putpixel = img.putpixel
    img_x, img_y = img.size

    # seeds = [[], []]
    # generate seeds
    # draw.rectangle([(startx, starty), (endx, endy)], fill=(r, g, b))

    seeds = []

    for i in range(num_seeds):
        seed1 = Seed(0, 0, 0, 0, 0, draw, putpixel)
        seed1.setColor()
        seed1.setLocation(w, h)
        # draw.rectangle([(seed1.getLocation()[0]-50, seed1.getLocation()[1]-50), (seed1.getLocation()[0]+50, seed1.getLocation()[1]+50)], fill=(seed1.getColor()[0], seed1.getColor()[1], seed1.getColor()[2]))
        seed1.drawCenter()
        seeds.append(seed1)

    for seed in seeds:
        for i in range(img_x):
            for j in range(img_y):
                # euclid distance pixel to every single seed
                # record the min seed
                # assign pixel to color of min seed
                coords = (i, j)
                seed_coords = seed.getLocation()

                dist = seed.euclideanDistance(coords[0], coords[1], seed_coords[0], seed_coords[1])
                print(dist)

    img.save("test.png", "PNG")




generate_euclid(500, 500, 1)
