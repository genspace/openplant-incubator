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
from incubator.raspberrypi.scripts import BASE_CONFIG
from incubator.util import get_connection_string

from contextlib import contextmanager
from sqlalchemy.orm import scoped_session, sessionmaker


# Create library object using our Bus I2C port
sensor = None
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = HTU21D(i2c)
except ValueError:
    logger.info("Please enable I2C Bus and Camera...")
    logger.info("Launching config in 3 seconds...")
    time.sleep(3)
    os.system("sudo raspi-config")

try:
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = HTU21D(i2c)
except ValueError as e:
    logger.error("I2C not enabled... will not log sensor values to database")
    pass


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
CAMERA_FREQ_SECONDS = int(config_params['camera_freq_seconds'])
SENSOR_FREQ_SECONDS = int(config_params['sensor_freq_seconds'])
LIGHT_TIME = tuple(
    map(int, config_params.get('light_time', "800,2399").split(","))
)
CAMERA_RESOLUTION = tuple(
    map(int, config_params.get('camera_resolution', "1280,720").split(","))
)

# Set paths for folder upload
S3_PATH = f"s3://openplant/images/{INCUBATOR_NAME}-{uuid.getnode()}"


@contextmanager
def get_db_session():
    """ Creates a context with an open SQLAlchemy session.
    """
    engine = create_engine(get_connection_string(), convert_unicode=True)
    connection = engine.connect()
    db_session = Session(
        autocommit=False,
        autoflush=True,
        bind=engine
    )
    yield db_session
    db_session.close()
    connection.close()


def validate_incubator_name():
    # Ensure incubator name is valid
    bad_char_list = [" ", "/", "\\"]
    if len(set(bad_char_list) & set(INCUBATOR_NAME)) > 0:
        raise ValueError(f"Incubator name cannot contain: {bad_char_list}")
    if not INCUBATOR_NAME:
        raise ValueError("Missing incubator name!")


def initialize_system():
    # Ensure picture folder exists
    os.system("mkdir -p " + PICTURES_FOLDER)
    # Lights as output and off
    os.system("gpio -g mode 12 out")
    os.system("gpio -g write 12 0")


def check_incubator_id():
    incubator_id = None
    with get_db_session() as session:
        result = (
            session.query(schema.Incubator.id)
            .filter(schema.Incubator.node == uuid.getnode())
            .first()
        )
        if result:
            incubator_id = result[0]
    return incubator_id


def get_incubator_id():
    # Check to see if incubator name exists in database, if not, create
    incubator_id = check_incubator_id()
    if not incubator_id:
        try:
            with get_db_session() as session:
                logger.info("Incubator ID not yet created... assigning new")
                incubator = schema.Incubator(name=INCUBATOR_NAME, node=uuid.getnode())
                session.add(incubator)
                session.commit()
                incubator_id = check_incubator_id()
        except Exception as e:
            logger.error(e)
            raise(Exception('Could not load incubator ID. Ensure name is unique!'))
    return incubator_id


def is_lights_on():
    now = datetime.datetime.now()
    time_int = int(now.strftime("%H%M"))
    return (time_int >= LIGHT_TIME[0]) & (time_int <= LIGHT_TIME[1])


def take_picture():
    # Attempt to take picture of plant
    t_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{t_stamp}.jpg"
    src_path = os.path.join(PICTURES_FOLDER, filename)
    dst_path = "/".join([S3_PATH, filename])
    took_pic = False
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = CAMERA_RESOLUTION
            camera.capture(src_path)
        took_pic = True
    except picamera.exc.PiCameraError as err:
        logger.error("Error taking picture: " + str(err))
    if took_pic:
        os.system(f"aws s3 cp {src_path} {dst_path}")
        logger.info(f"Uploaded picture to: {dst_path}")
        os.system(f"rm {src_path}")
    return took_pic


def adjust_lights():
    if is_lights_on():
        # logger.info("Lights on")
        os.system("gpio -g write 12 1")
    else:
        # logger.info("Lights off")
        os.system("gpio -g write 12 0")


def write_to_database(incubator_id) -> bool:
    """Attempt to write to database, if not successful log failure."""
    record = schema.Sensor(
        incubator_id = incubator_id,
        time = datetime.datetime.now(),
        temperature = sensor.temperature,
        humidity = sensor.relative_humidity,
        light = int(is_lights_on()),
    )
    is_success = True
    try:
        with get_db_session() as session:
            session.add(record)
            session.commit()
            logger.info(record)
    except Exception as e:
        logger.error(e)
        logger.error('Failed to write to database, will attempt on next cycle!')
        is_success = False
    return is_success


def main(max_retry=5):
    cowsay.tux("Let's incubate!")
    validate_incubator_name()
    initialize_system()
    incubator_id = get_incubator_id()
    camera_time = (time.time() - CAMERA_FREQ_SECONDS)
    sensor_time = (time.time() - SENSOR_FREQ_SECONDS)
    while True:
        adjust_lights()
        # take picture if necessary
        camera_delta = (time.time() - camera_time)
        if ((camera_delta > CAMERA_FREQ_SECONDS) or (camera_retry > 0 and camera_retry < max_retry)):
            if is_lights_on():
                if take_picture():
                    camera_time, camera_retry = (time.time(), 0)
                else:
                    camera_retry += 1
                if camera_retry >= max_retry:
                    camera_retry = 0
        # log sensor data if necessary
        sensor_delta = (time.time() - sensor_time)
        if sensor and ((sensor_delta > SENSOR_FREQ_SECONDS) or (sensor_retry > 0 and sensor_retry < max_retry)):
            if write_to_database(incubator_id):
                sensor_time, sensor_retry = (time.time(), 0)
            else:
                sensor_retry += 1
            if sensor_retry >= max_retry:
                sensor_retry = 0
        # logger.info(f"System heartbeat: {datetime.datetime.now()}")
        time.sleep(5)

if __name__ == "__main__":
    main()
