from photo_pipeline import calculation as ccl
import os
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective, contours
import numpy as np
import argparse
import imutils
import cv2
import matplotlib.image as mpimg

if __name__=='__main__':

    img = "20190525_153521.jpg"
    image = cv2.imread(img) 
    is_ = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # plant color 
    colors_small = ccl.color_hist(image)
    max_green = max(colors_small)
    area_small = ccl.get_area_green(colors_small)

    # plant size
    bounding_box = ccl.size_detect(image, width = 3.93701, fname = "out2.png")

    print("Area: ", area, " Size: ", bounding_box)
