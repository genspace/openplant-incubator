#!/usr/env/bin python3

"""
Main utility for logging sensor data to database /
regular picture uploads.
"""

import datetime
import configparser
from loguru import logger
import os
import time
import uuid

from adafruit_htu21d import HTU21D
import board
import busio
import cowsay
from dotenv import load_dotenv
import picamera
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from models import schema
from incubator.raspberrypi.scripts import BASE_CONFIG, SCRIPT_DIR
from incubator.util import get_connection_string


# Ensure pip installs available
os.system("install-requirements")


# Create library object using our Bus I2C port
sensor = None
while not sensor:
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        sensor = HTU21D(i2c)
    except ValueError:
        logger.info("Please enable I2C bus")
        os.system("sudo raspi-config")


# Get config
def read_config():
    # get config path
    base_config = configparser.ConfigParser()
    base_config.read(BASE_CONFIG)
    base_keys = list(base_config['BASE'].keys())
    # set config if not exists
    if not ('config_path' in base_keys and 'cred_path' in base_keys):
        os.system('set-config')
    base_config.read(BASE_CONFIG)
    config_path = base_config['BASE']['config_path']
    cred_path = base_config['BASE']['cred_path']
    # read config
    config = configparser.ConfigParser()
    config.read(config_path)
    load_dotenv(cred_path)
    return dict(config['INCUBATOR'])


# Unpack config values
config_params = read_config()
INCUBATOR_NAME = config_params['incubator_name']
PICTURES_FOLDER = config_params['pictures_folder']
SLEEP_INTERVAL_SEC = int(config_params['sleep_interval_sec'])
LIGHT_TIME = tuple(
    map(int, config_params['light_time'].split(","))
)

# Set paths for folder upload
S3_PATH = f"s3://openplant/images/{INCUBATOR_NAME}-{uuid.getnode()}"

# Create database session
engine = create_engine(get_connection_string())
session = Session(bind=engine)


def validate_incubator_name():
    # Ensure incubator name is valid
    bad_char_list = [" ", "/", "\\"]
    if len(set(bad_char_list) & set(INCUBATOR_NAME)) > 0:
        raise ValueError(f"Incubator name cannot contain: {bad_char_list}")
    if not INCUBATOR_NAME:
        raise ValueError("Missing incubator name!")


def initialize_system():
    # Ensure picture folder exists
    os.system("sudo mkdir -p " + PICTURES_FOLDER)
    # Lights as output and off
    os.system("gpio -g mode 12 out")
    os.system("gpio -g write 12 0")


def get_incubator_id():
    # Check to see if incubator name exists in database, if not, create
    def query_id():
        return (
            session.query(schema.Incubator.id)
            .filter(schema.Incubator.node == uuid.getnode())
            .first()
        )
    incubator_id = query_id()
    if not incubator_id:
        logger.info("Incubator ID not yet created... assigning new")
        incubator = schema.Incubator(name=INCUBATOR_NAME, node=uuid.getnode())
        session.add(incubator)
        session.commit()
        incubator_id = query_id()
    return incubator_id[0]


def take_picture():
    # Attempt to take picture of plant
    t_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{t_stamp}.jpg"
    src_path = os.path.join(PICTURES_FOLDER, filename)
    dst_path = "/".join([S3_PATH, filename])
    took_pic = False
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.capture(src_path)
        took_pic = True
    except picamera.exc.PiCameraError as err:
        logger.error("Error taking picture: " + str(err))
    except:
        logger.error("Error taking picture.")
    if took_pic:
        os.system(f"aws s3 cp {src_path} {dst_path}")
        logger.info(f"Uploaded picture to: {dst_path}")
        os.system("rm {src_path}")


def is_lights_on():
    now = datetime.datetime.now()
    time_int = int(now.strftime("%H%M"))
    return (time_int >= LIGHT_TIME[0]) & (time_int <= LIGHT_TIME[1])


def adjust_lights():
    if is_lights_on():
        logger.info("Lights on")
        os.system("gpio -g write 12 1")
    else:
        logger.info("Lights off")
        os.system("gpio -g write 12 0")


def write_to_database(incubator_id):
    record = schema.Sensor(
        incubator_id = incubator_id,
        time = datetime.datetime.now(),
        temperature = sensor.temperature,
        humidity = sensor.relative_humidity,
        light = int(is_lights_on()),
    )
    session.add(record)
    session.commit()
    logger.info(record)


def main():
    cowsay.tux("Let's incubate!")
    validate_incubator_name()
    initialize_system()
    incubator_id = get_incubator_id()
    while True:
        adjust_lights()
        take_picture()
        write_to_database(incubator_id)
        time.sleep(SLEEP_INTERVAL_SEC)


if __name__ == "__main__":
    main()
