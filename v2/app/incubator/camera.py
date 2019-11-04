import picamera
import datetime
import os
import time


def take_picture():
    t = datetime.datetime.now()
    filename = "{some-folder}" + t.strftime("%Y_%M_%d_%H_%M_%S_%f") + ".jpg"
    print("filename: ", filename)
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(filename)
    print("picture taken")
    os.system("{s3-upload}".format(filename))

while True:
    take_picture()
    time.sleep(300)


