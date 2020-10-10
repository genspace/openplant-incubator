import picamera
import datetime
import os
import time

from config import *

os.system("mkdir -p " + PICTURES_FOLDER)

S3FOLDER = "s3://brooklyn.openplant.monitor.camera/piV3pics/" + INCUBATOR_NAME
S3UPLOAD = "aws s3 cp {} " + S3FOLDER

def initialize():
    # Lights as output and off
    os.system("gpio -g mode 12 out");
    os.system("gpio -g write 12 0");

def take_picture():
    t = datetime.datetime.now()
    filename = PICTURES_FOLDER + "/" + PLANT_NAME + "_" + \
        t.strftime("%Y_%m_%d_%H_%M_%S_%f") + ".jpg"
    print("filename: ", filename)

    took_pic = False

    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1280,720)
            camera.capture(filename)
        took_pic = True
    except picamera.exc.PiCameraError as err:
        print("Error taking picture: " + str(err))
    except:
        print("Error taking picture.")

    if took_pic:
        print("picture taken")
        os.system(S3UPLOAD.format(filename))
        os.system("rm " + filename)

def adjust_lights():
    hour = datetime.datetime.now().hour
    # Ligths are on after 8am (hour is from [00 .. 23]
    if hour > 8:
        print("Lights on");
        os.system("gpio -g write 12 1");
    else :
        print("Lights off");
        os.system("gpio -g write 12 0");

initialize()

while True:
    adjust_lights()
    take_picture()
    time.sleep(SLEEP_INTERVAL_SEC)
