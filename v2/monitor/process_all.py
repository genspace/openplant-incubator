from photo_pipeline import processing as pc 
from photo_pipeline import calculation as calc 
from PIL import Image
import time
import matplotlib.image as mpimg
import fire
import cv2
import os
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import imutils
import math
import pandas as pd
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np

def start(img_name):
    
    start = time.time()
    
    processed_img = process_img(img_name)
    metrics, final_img = get_size_health(processed_img)
    
    img_pcd_name = "data/processed/" + ''.join(img_name.split(".")[:-1]) + "_pcd"  + '.jpg'
    mpimg.imsave(img_pcd_name, processed_img/255)
    os.system("aws s3 cp {0} {1}".format(img_pcd_name, os.environ["OPBUCKET"]))
    os.system("rm {0}".format(img_pcd_name))
    
    img_final_name = "data/final/" +  ''.join(img_name.split(".")[:-1]) + "_final" + '.jpg'
    mpimg.imsave(img_final_name, final_img/255)
    os.system("aws s3 cp {0} {1}".format(img_final_name, os.environ["OPBUCKET"]))
    os.system("rm {0}".format(img_final_name))
    
    df = pd.read_csv("./data/metrics.csv")
    result = pd.concat([df, metrics], ignore_index = True, sort = False)
    result.to_csv("./data/metrics.csv", index = False)
    
    print(time.time() - start)
    
def identification():
    
    band_pic, cser = band_wrap(img, circle)
    band_ct = count_bands(cser)
    
def process_img(img_name):

    img_raw = cv2.imread("data/raw/" + img_name, cv2.IMREAD_COLOR)
    img, circle = pc.prep_image(img_raw)
    img_circle = pc.draw_circle(img, circle)

    return(img_circle)

def get_size_health(image):

    # Detect plant
    dark_green = np.array([23,28,26])
    light_green = np.array([144,238,144])
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV) #cv2.COLOR_BGR2HSV
    mask = cv2.inRange(hsv, dark_green, light_green)
    res = cv2.bitwise_and(image, image, mask = mask)
    
    # Calculate size 
    dish_size_pixels = math.pi*(res.shape[0]/2)**2
    dish_area_actual_mm = (math.pi*45**2)
    plant_size_per_pixels = np.sum(res.ravel() > 0)/dish_size_pixels
    plant_size_actual_mm = round(plant_size_per_pixels*dish_area_actual_mm, 2)
    
    # Calculate health
    colors = calc.color_hist(image)
    plant_green_area = calc.get_area_green(colors)
    
    data = pd.DataFrame({'plant': ["test.png"], 'size': [plant_size_actual_mm], 'health': [plant_green_area]})
    
    return((data, res))

if __name__ == "__main__":
    fire.Fire(start)

