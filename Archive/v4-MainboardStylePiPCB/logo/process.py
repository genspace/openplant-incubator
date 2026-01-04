#!/usr/bin/python3

from PIL import Image;

img = Image.open("liverwort.jpg")
pixels = img.load() # create the pixel map

width = img.size[0]
height = img.size[1]

def get_avg_around(i,j):
    avg = 0
    side = 5
    i = int(i / side) * side
    j = int(j / side) * side
    for dx in range(0, side):
      for dy in range(0, side):
        if (i + dx < width and j + dy < height):
          avg += (pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2]) / 3
    avg = int(avg / side / side)
    return avg

def get_pixel(i,j):
    avg = 0
    if (i < width and j < height):
        avg = (pixels[i,j][0] + pixels[i,j][1] + pixels[i,j][2]) / 3
        avg = int(avg)
    return avg

def edge_pixel(i,j):
    return get_pixel(i,j) - get_pixel(i+4, j) + get_pixel(i, j) - get_pixel(i, j+4)
  
for i in range(width):    # for every col:
  for j in range(height):    # For every row
    edg = edge_pixel(i, j)
    avg = get_avg_around(i,j)
    if (edg > 100):
        pixels[i,j] = (200, 200, 200)
    elif (edg > 50):
        pixels[i,j] = (200, 200, 0)
    else:
        pixels[i,j] = (0, 150, 0)

    # pixels[i,j] = (150, 150, 0)
    # pixels[i,j] = (edg, int(150 - edg / 2), int(150 - edg / 2))

img.save("bla.png")
