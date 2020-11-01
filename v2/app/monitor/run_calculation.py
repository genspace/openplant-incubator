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
    
def run_calculation(img_path):
    
    image = cv2.imread(img_path) 
    results = ccl.calculation(image)

    return(img_path, results)

if __name__=='__main__':
    
    fire.Fire(run_calculation)
