#!/usr/env/bin python3

"""
Script to take data from serial and load
into the database
"""

import re
import os
import time
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

#-set sleep time
SLEEP_TIME = 60 * 60

#-get incubator id from environment
incubator_number = os.environ['INCUBATOR_NUMBER']

#-connect to database
engine = create_engine(get_connection_string())
session = Session(bind=engine)

#-get incubator id
def get_incubator_id():
    query_result =\
        session.query(Incubator.id)\
               .filter(Incubator.number == incubator_number)\
               .first()
    if query_result:
        incubator_id = query_result[0]
        logger.info('Incubator ID: {}'.format(incubator_id))
    #-add to database if not exists
    elif re.match('\d+$', incubator_number):
        logger.info('Encountered new incubator number: {}'
                    .format(incubator_number))
        logger.info('Adding to database')
        obj = Incubator()
        obj.number = incubator_number
        session.add(obj)
        session.commit()
        #-get updated incubator value
        incubator_id = get_incubator_id()
        logger.info('Added new incubator: {}'.format(incubator_id))
    else:
        logger.error('Invalid incubator number: {}'
                     .format(incubator_number))
        raise ValueError('INVALID INCUBATOR NUMBER!')
    return incubator_id

#-create connection to serial drive
ser = serial.Serial('/dev/ttyUSB0', 9600)

#-set regex map to parse label input
regex_map = [
    ('temperature', r'Temp.*=\s+([\d\.]+)', ),
    ('humidity', r'Hum.*=\s+([\d\.]+)', ),
    ('light', r'lights are (\w+)', ),
]

label_translation = [
    ('light', lambda e: int(e == 'on'))
]


def add_line_to_dict(e, value_dict):
    """
    Simple function to parse serial line
    """
    for label, regex in regex_map:
        reg = re.search(regex, e)
        if reg:
            #-get matched regex value
            val = reg.group(1)
            #-translate value if in label translation
            if label in dict(label_translation).keys():
                val = dict(label_translation)[label](val)
            #-add to dictionary
            value_dict[label] = val
            #-log output
            logger.info('Parsed: ({}, {})'.format(label, val))
            break
    return value_dict


def check_dict_completion(value_dict):
    """
    Check to see if all values are in record
    """
    keys = set(value_dict.keys())
    labels = set([e[0] for e in regex_map])
    return len(labels - keys) == 0


def upload_record_to_database(value_dict, incubator_id):
    """
    Build upload object and add to database
    """
    obj = Sensor()
    obj.incubator_id = incubator_id
    obj.time = dt.datetime.today()
    for k, v in value_dict.items():
        setattr(obj, k, v)
    logger.info(str(obj))
    session.add(obj)
    session.commit()
    return obj


def main():
    """
    Parse the lines and add to the database forever
    """
    ser.flushInput()
    value_dict = dict()
    logger.info('initiating main sequence')
    incubator_id = get_incubator_id()
    while 1:
        logger.info(ser.in_waiting)
        if (ser.in_waiting > 0):
            logger.info('reading serial')
            line = ser.readline().decode("utf-8")
            logger.info(line)
            add_line_to_dict(line, value_dict)
            logger.info(str(value_dict))
        if check_dict_completion(value_dict):
            logger.info('loading values to db')
            obj = upload_record_to_database(value_dict, incubator_id)
            logger.info('loaded: {}'.format(obj))
            value_dict = dict()
            time.sleep(SLEEP_TIME)
            ser.flushInput()
    return None


if __name__ == '__main__':
    main()
