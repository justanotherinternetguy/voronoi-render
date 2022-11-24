from PIL import Image
import random
import math

def generate_euclid(w, h, num_seeds):
    img = Image.new("RGB", (w, h))
    putpixel = img.putpixel
    img_x, img_y = img.size

    # seeds = [[], []]
    # generate seeds

    seeds = []
    r, g, b = [], [], []

    for i in range(num_seeds):
        seeds.append([random.randint(0, w), random.randint(0, h)])
        r.append(random.randint(256))
        g.append(random.randint(256))
        b.append(random.randint(256))

    for k in range(len(seeds)):


    print(seeds)

    img.save("test.png", "PNG")




generate_euclid(500, 500, 15)
