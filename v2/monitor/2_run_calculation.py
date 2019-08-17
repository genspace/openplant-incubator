import os
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import analysis as anls
import matplotlib.image as mpimg

if __name__=='__main__':

    img = "20190525_153521.jpg"
    image = cv2.imread("../../data/raw/" + img) 
    is_ = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image);

    # plant color 
    colors_small = anls.color_hist(image)
    max_green = max(colors_small)
    area_small = anls.get_area_green(colors_small)

    # plant size
    bounding_box = anls.size_detect(image, width = 3.93701, fname = "out2.png")