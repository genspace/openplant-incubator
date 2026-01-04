import os
import cv2
import time
import logging
import numpy as np
import pandas as pd
from math import atan2, pi, sqrt
from matplotlib import pyplot as plt

def process(img_raw):

    img, circle = prep_image(img_raw)
    img_circle = draw_circle(img, circle) 
    
    return(img_circle)

def apply_hough_transform(img, min_rad=500, max_rad = None):
    """
    Get the top resulting cricle from the hough circle transform
    """
    # Get max rad
    if max_rad is None: max_rad = img.shape[0] // 2
    # Convert to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image to reduce noise
    img_blur = cv2.medianBlur(gray, 5)
    # Get the circles
    circles =\
        cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1,
                         img.shape[0], param1=200, param2=10,
                         minRadius=500, maxRadius=img.shape[0]//2)
    # Return the top circle
    top_circle = circles[0][0]
    
    return top_circle


def circle_crop(img, circle, buffer = 0.1):
    """
    Take input image and tuple that defines (x, y, r) of circle.
    Buffer extends radius around center of circle and removes all outside of that zone.
    """
    x, y, r = circle
    # crop image
    buffer = max([buffer, 0]) + 1
    y_top = int(y - r * buffer)
    y_bottom = int(y + r * buffer)
    x_left = int(x - r * buffer)
    x_right = int(x + r * buffer)
    img_out = img[y_top:y_bottom, x_left:x_right].copy()
    # adjust circle coordinates
    new_xy = int(0 + r * buffer) + 0.5
    circle = np.array([new_xy, new_xy, r])
    
    return img_out, circle

def circle_strip(img, circle, buffer=.1,
                 background=(255, 255, 255), alpha=0):
    """
    Take input image and tuple that defines (x, y, r) of circle.
    If crop, remove all pixels outside of circle with alpha value.
    Buffer defines square around center that will not be cropped.
    If not crop, set all pixels outside of the cirlce to background.
    """
    x, y, r = circle
    img_out = []
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    for iy, _ in enumerate(img):
        img_x = []
        for ix, _ in enumerate(img[iy]):
            pix = img[iy][ix]
            if (ix - x) ** 2 + (iy - y) ** 2 > r ** 2:
                if background is not None:
                    pix = list(background)
                    pix.append(255)
                if alpha is not None:
                    pix[3] = alpha
            img_x.append(pix)
        img_out.append(img_x)
    img_out = np.array(img_out)
    img_out = np.uint16(np.around(img_out))
    
    return img_out


def draw_circle(img, circle, center=True):
    """
    Take image and circle, draw green outer perimeter,
    put red dot in center
    """
    img_out = img.copy()
    circle = np.uint16(np.around(circle))
    if img.shape[2] == 3:
        outer_color = (0, 255, 0)
        innner_color = (255, 0, 0)
    elif img.shape[2] == 4:
        outer_color = (0, 255, 0, 255)
        innner_color = (255, 0, 0, 255)
    else:
        return img
    # Draw outer circle
    # cv2.circle(img_out, (circle[0], circle[1]),
    #            circle[2], outer_color, img.shape[0] // 100)
    # if center:
    #     # Draw inner circle
    #     cv2.circle(img_out, (circle[0], circle[1]),
    #                4, innner_color, img.shape[0] // 50)
                   
    return img_out

def prep_image(img_raw):    
    circle = apply_hough_transform(img_raw)
    img, circle = circle_crop(img_raw, circle)
    img = circle_strip(img, circle)
    
    return img, circle
