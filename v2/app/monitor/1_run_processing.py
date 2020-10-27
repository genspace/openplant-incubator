from photo_pipeline import processing as pcs
import cv2
from PIL import Image
import matplotlib.image as mpimg
import fire
import os.path
    
def run_processing(img_path):

    img_raw = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_circle, output_path = pcs.process(img_raw)
    
    mpimg.imsave(output_path, img_circle/255)
    
    return(1)

if __name__ == "__main__":
    
    fire.Fire(run_processing)

