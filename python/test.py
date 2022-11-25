
for i in range(img_x):
    for j in range(img_y):
        for s in range(len(seeds) - 1):
            # euclid distance pixel to every single seed
            # record the min seed
            # assign pixel to color of min seed
            coords = (i, j)
            seed_coords = seeds[s].getLocation()
            seed_coords_1 = seeds[s+1].getLocation()

            dist1 = seeds[s].euclideanDistance(coords[0], coords[1], seed_coords[0], seed_coords[1])
            dist2 = seeds[s+1].euclideanDistance(coords[0], coords[1], seed_coords_1[0], seed_coords_1[1])
            nearest = min(dist1, dist2)

            if nearest == dist1:
                putpixel(coords, seeds[s].getColor())
                seeds[s].drawCenter()
            else:
                putpixel(coords, seeds[s+1].getColor())
                seeds[s+1].drawCenter()