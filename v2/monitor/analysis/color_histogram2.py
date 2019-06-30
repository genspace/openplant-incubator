from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def color_hist(image):
    # grab the image channels, initialize the tuple of colors,
    # the figure and the flattened feature vector
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title("'Flattened' Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    features = []

    # loop over the image channels
    for (chan, color) in zip(chans, colors):
        
        if color != 'g': continue
        # create a histogram for the current channel and
        # concatenate the resulting histograms for each
        # channel
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        
        print("max green: ", max(hist))
        
        features.extend(hist)

        # plot the histogram
        plt.plot(hist, color = color)
        plt.xlim([0, 256])
        plt.ylim([0, 900000])
        
    return(features)

green_area = lambda color_hist: np.trapz([pixel_val[0] for pixel_val in color_hist])
 
