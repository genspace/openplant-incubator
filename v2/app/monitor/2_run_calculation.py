# python 2_run_calculation.py --img_name=cropped_IMG_20200326_174326.jpg
# Area:  9532650.0  Size:  5.57998884 in^2, 141 mm^2p

from photo_pipeline import calculation as ccl
import os
from scipy.spatial import distance as dist
from imutils import perspective, contours
import numpy as np
import argparse
import imutils
import cv2
import fire
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

def calculate(img_name):
    
    image = cv2.imread(img_name) 
    #is_ = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # plant color 
    colors_small = ccl.color_hist(image)
    max_green = max(colors_small)
    area_small = ccl.get_area_green(colors_small)

    # plant size
    # width in inches for 100mm plate: 3.93701
    # width in inches for 60mm plate: 2.3622
    bounding_box = ccl.size_detect(image, width = 2.3622, fname = "out2.png")

    print("Area: ", area_small, " Size: ", bounding_box)
    
    return(1)

if __name__=='__main__':
    fire.Fire(calculate)


