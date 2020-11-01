from photo_pipeline import calculation as ccl
import os
import numpy as np
import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from skimage.color import rgb2gray, gray2rgb
from plantcv import plantcv as pcv
from skimage.filters import sobel, gaussian
from skimage.feature import canny
from skimage.morphology import binary_opening
from scipy import ndimage as ndi
from PIL import Image, ImageOps
from toolz import pipe

def get_area(img, img_diameter):
    
    plate_diameter_mm = 60
    
    calculate_area = lambda x: pipe(
    sum(np.ravel(x) != 0), 
    lambda a: a*(np.pi*(plate_diameter_mm/2)**2)/(np.pi*(img_diameter/2)**2), 
    lambda b: round(b, 2)
    )
    
    result = calculate_area(img)
    
    return(result)

def calculation(image):
    
    PIL_image = Image.fromarray(np.uint8(image)).convert('RGB')
    invert_im = ImageOps.invert(PIL_image) # invert image (so that white is 0)
    imageBox = invert_im.getbbox()
    cropped = PIL_image.crop(imageBox)
    image = np.asanyarray(cropped)
    
    s = pcv.rgb2gray_hsv(rgb_img = image, channel = 's')
    s_thresh = pcv.threshold.binary(gray_img = s, threshold = 150, max_value = 255, object_type = 'light')
    area = get_area(s_thresh, s_thresh.shape[0])
    
    img2 = np.copy(image)
    img2[s_thresh == 0] = 0
    health = get_area(img2[:,:,1], s_thresh.shape[0])
    
    results = {"healthy_size": health, "size": area}
    
    return(results)

