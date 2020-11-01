import os
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

def calculation(image):

    # plant color 
    colors_small = color_hist(image)
    area_small = get_area_green(colors_small)

    # plant size
    # width in inches for 60mm/100mm plate: 2.3622/3.93701
    bounding_box = size_detect(image, width = 2.3622, fname = "out.png")
    
    results = {"healthy_area": area_small, "size": bounding_box}
    
    return(results)
