from photo_pipeline import processing as pcs
from PIL import Image
import time
import matplotlib.image as mpimg
import click
    
@click.command()
@click.option('--img')
@click.option('--fn')
def get_data(img, fn):
    return(img, fn)

def identification():
    
    band_pic, cser = band_wrap(img, circle)
    band_ct = count_bands(cser)
    
def main():

    img = "20190525_153521.jpg"
    img_raw = cv2.imread(img, cv2.IMREAD_COLOR)
    img, circle = pcs.prep_image(img_raw)
    img_circle = pcs.draw_circle(img, circle) 
  
    mpimg.imsave("cropped_" + img, img_circle/255)

if __name__ == "__main__":
    main()

