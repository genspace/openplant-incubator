import picamera
import datetime
import os
import time


def take_picture():
    t = datetime.datetime.now()
    filename = "pictures/" + t.strftime("%Y_%m_%d_%H_%M_%S_%f") + ".jpg"
    print("filename: ", filename)
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(filename)
    print("picture taken")
    os.system(os.environ["S3UPLOAD"].format(filename))
    os.system("rm pictures/*")

while True:
    take_picture()
    time.sleep(300)


