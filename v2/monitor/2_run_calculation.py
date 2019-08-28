from photo_pipeline import calculation as calc 
import os
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
import matplotlib.image as mpimg
import fire
import math
import time
import pandas as pd
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np

def get_size_health(img_name):
    
    start = time.time()

    image = cv2.imread("./data/processed/" + img_name) 

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
    
    # Export results
    data = pd.DataFrame({'plant': ["test.png"], 'size': [plant_size_actual_mm], 'health': [plant_green_area]})
    #data.to_csv("./data/metrics.csv")
    df = pd.read_csv("./data/metrics.csv")
    result = pd.concat([df, data], ignore_index = True, sort = False)
    result.to_csv("./data/metrics.csv", index = False)
    
    img_final_name = ''.join(img_name.split(".")[:-1]) + "_final"
    mpimg.imsave("data/final/" + img_final_name + '.jpg', res/255)
    
    print(time.time() - start)

if __name__=='__main__':
    fire.Fire(get_size_health)

