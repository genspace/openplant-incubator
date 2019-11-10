from funcs_processing import * 
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

    print(5)

    start = time.time()

    img, fname = "20190525_153521.jpg", "test.png"

    print(img, fname)

    img_raw = cv2.imread("../data/raw/" + img, cv2.IMREAD_COLOR)
    img, circle = prep_image(img_raw)
    img_circle = draw_circle(img, circle)
    
    #plt.imshow(img_raw) plt.show(img_circle)
    
    mpimg.imsave("../data/processed/" + fname, img_circle/255)

    print(time.time() - start)

if __name__ == "__main__":
    main()

