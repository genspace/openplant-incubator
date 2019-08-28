from photo_pipeline import processing as pc 
from PIL import Image
import time
import matplotlib.image as mpimg
import fire
import cv2
import matplotlib.image as mpimg
    
def get_data(img, fn):
    return(img, fn)

def identification():
    
    band_pic, cser = band_wrap(img, circle)
    band_ct = count_bands(cser)
    
def process_img(img_name):
    
    #image name of the form: "20190525_153521.jpg"
    
    start = time.time()

    img_raw = cv2.imread("data/raw/" + img_name, cv2.IMREAD_COLOR)
    img, circle = pc.prep_image(img_raw)
    img_circle = pc.draw_circle(img, circle)
    #plt.imshow(img_raw) 
    #plt.show(img_circle)
    
    img_pcd_name = ''.join(img_name.split(".")[:-1]) + "_pcd"
    mpimg.imsave("data/processed/" + img_pcd_name + '.jpg', img_circle/255)

    print(time.time() - start)

if __name__ == "__main__":
    fire.Fire(process_img)

