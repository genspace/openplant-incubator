#!/bin/bash

set -a &&\
  source db.env &&\
  docker-compose build
