#!/usr/env/bin python3

"""
Script to take data from serial and load
into the database
"""

import re
import os
import uuid
import serial
import logging
import datetime as dt
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from app.util import get_connection_string
from app.models.schema import Sensor, Incubator

#-set logger
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#-get incubator id from environment
incubator_number = os.environ['INCUBATOR_NUMBER']

#-connect to database
engine = create_engine(get_connection_string())
session = Session(bind=engine)

#-get incubator id
incubator_id = session.query()

#-create connection to serial drive
ser = serial.Serial('/dev/ttyUSB0', 9600)

#-set regex map to parse label input
regex_map = [
    ('temperature', r'^Temp.* = ([\d\.]*)$', ),
    ('humidity', r'^Hum.* = ([\d\.]*)$', ),
    ('light', r'lights are (\w+)', ),
]


def add_line_to_dict(e, value_dict):
    """
    Simple function to parse serial line
    """
    for label, regex in regex_map:
        reg = re.search(e, regex)
        if reg:
            val = reg.group(1)
            value_dict.update({label: val})
            logger.info(f'Parsed: ({label}, {val})')
            return value_dict
    return None


def check_dict_completion(value_dict):
    """
    Check to see if all values are in record
    """
    keys = set(value_dict.keys())
    labels = set([e[0] for e in regex_map])
    return len(labels - keys) == 0


def upload_record_to_database(value_dict):
    obj = Sensor()
    obj.incubator_id = incubator_id
    obj.time = dt.datetime.today()
    for k, v in value_dict.items():
        setattr(obj, k, v)
    session.add(obj)
    session.commit()
    return obj


def main():
    """
    Parse the lines and add to the database forever
    """
    ser.flushInput()
    value_dict = dict()
    while 1:
        if(ser.in_waiting > 0):
            line = ser.readline().decode("utf-8")
            logger.info(line)
            add_line_to_dict(line, value_dict)
        if check_dict_completion(value_dict):
            obj = upload_record_to_database(value_dict)
            logger.info(f'Loaded: {obj}')
        value_dict = dict()
    return None

if __name__ == '__main__':
    main()
