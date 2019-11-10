#!/bin/bash

set -a && \
    source db.env && \
    source incubator.env && \
    python3 app/incubator/raspberrypi/log_sensor_data.py
