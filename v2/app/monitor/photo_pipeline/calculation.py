import os
from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# Plant Color Density Histogram: https://bit.ly/2ENtVXr
# Object Size: https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/

def midpoint(ptA, ptB):

	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def get_area_green(color_features):
	"""
	Gets area of green channel of image from the output of color_hist
	"""
	result = np.trapz([pixel_val[0] for pixel_val in color_features])

	return(result)

def color_hist(image):

	# old code where the param is a path

    #image = cv2.imread(path)
    # convert the image to grayscale and create a histogram
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #plt.imshow(image)
    #plt.title('Pic')
    #plt.show()

#   hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
#   plt.figure()
#   plt.title("Grayscale Histogram")
#   plt.xlabel("Bins")
#   plt.ylabel("# of Pixels")
#   plt.plot(hist)
#   plt.xlim([0, 256])

	# actual code

    # grab the image channels, initialize the tuple of colors,
    # the figure and the flattened feature vector
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    features = []

    #plt.figure()
    #plt.title("'Flattened' Color Histogram")
    #plt.xlabel("Bins")
    #plt.ylabel("# of Pixels")

    # loop over the image channels
    for (chan, color) in zip(chans, colors):
        
        if color != 'g': continue
        # create a histogram for the current channel and
        # concatenate the resulting histograms for each
        # channel
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        
        features.extend(hist)

        # plot the histogram
        #plt.plot(hist, color = color)
        #plt.xlim([0, 256])
        #plt.ylim([0, 900000])
        
    return(features)

def size_detect(image, width = 3.93701, fname = "out2.png"):
    """
    width is inches equivalent to 100mm since we're using p100 petri dishes
    """
    # load the image, convert it to grayscale, and blur it slightly
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv2.Canny(gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations = 1)
    edged = cv2.erode(edged, None, iterations = 1)

    # find contours in the edge map
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # sort the contours from left-to-right and initialize the
    # 'pixels per metric' calibration variable
    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric = None

    # loop over the contours individually
    for c in cnts:
        # if the contour is not sufficiently large, ignore it
        if cv2.contourArea(c) < 100: continue

        # compute the rotated bounding box of the contour
        orig = image.copy()
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")

        # order the points in the contour such that they appear
        # in top-left, top-right, bottom-right, and bottom-left
        # order, then draw the outline of the rotated bounding
        # box
        box = perspective.order_points(box)
        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

        # loop over the original points and draw them
        for (x, y) in box: cv2.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

        # unpack the ordered bounding box, then compute the midpoint
        # between the top-left and top-right coordinates, followed by
        # the midpoint between bottom-left and bottom-right coordinates
        (tl, tr, br, bl) = box
        (tltrX, tltrY) = anls.midpoint(tl, tr)
        (blbrX, blbrY) = anls.midpoint(bl, br)

        # compute the midpoint between the top-left and top-right points,
        # followed by the midpoint between the top-righ and bottom-right
        (tlblX, tlblY) = anls.midpoint(tl, bl)
        (trbrX, trbrY) = anls.midpoint(tr, br)

        # draw the midpoints on the image
        cv2.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        cv2.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

        # draw lines between the midpoints
        cv2.line(
            orig, 
            (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
            (255, 0, 255), 2)
        cv2.line(
            orig, 
            (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
            (255, 0, 255), 2)

        # compute the Euclidean distance between the midpoints
        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

        # if the pixels per metric has not been initialized, then
        # compute it as the ratio of pixels to supplied metric
        # (in this case, inches)
        if pixelsPerMetric is None: pixelsPerMetric = dB / width

        # compute the size of the object
        dimA = dA / pixelsPerMetric
        dimB = dB / pixelsPerMetric

        # draw the object sizes on the image
        cv2.putText(
            orig, 
            "{:.1f}in".format(dimA),
            (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
            0.65, (255, 255, 255), 2)
        cv2.putText(
            orig, 
            "{:.1f}in".format(dimB),
            (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
            0.65, (255, 255, 255), 2)

        # show the output image
        #plt.imshow(orig)
        #cv2.imshow("Image", orig)
        #cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('Image', 800,800)
        #cv2.waitKey(0)
        mpimg.imsave("../../data/bounded_imgs/" + fname, orig/255)
        
        return(box)
