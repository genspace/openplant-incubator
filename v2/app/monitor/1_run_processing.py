# python 1_run_processing.py --name=IMG_20200326_174326.jpg

import cv2
from photo_pipeline import processing as pcs
from PIL import Image
import time
import matplotlib.image as mpimg
import fire
import os.path

def identification():
    
    band_pic, cser = band_wrap(img, circle)
    band_ct = count_bands(cser)
    
    return(1)
    
def process(img_name):

    img_raw = cv2.imread(img_name, cv2.IMREAD_COLOR)
    img, circle = pcs.prep_image(img_raw)
    img_circle = pcs.draw_circle(img, circle) 
    output_path = os.path.dirname(img_name) + "/cropped_" + os.path.basename(img_name)
    
    mpimg.imsave(output_path, img_circle/255)
    
    return(1)

if __name__ == "__main__":
    fire.Fire(process)

