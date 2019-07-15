from processing import * 
from PIL import Image
import time
import matplotlib.image as mpimg
import click


def identification():
    
    band_pic, cser = band_wrap(img, circle)
    band_ct = count_bands(cser)
    
@click.command()
@click.option('--img')
def get_img(img):
    #'../data/raw/marpo_circle_1.jpg'
    return(img)
    
def main()

    start = time.time()

    img_file = get_img()
    img_raw = cv2.imread(img_file, cv2.IMREAD_COLOR)
    img, circle = prep_image(img_raw)
    img_circle = draw_circle(img, circle)
    
    plt.imshow(img_raw)
    #plt.show(img_circle)
    
    mpimg.imsave("../data/processed/out.png", img_circle/255)
    
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    

