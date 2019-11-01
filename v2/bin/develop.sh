#!/bin/bash

mkdir -p db-data
set -a && source db.env
docker-compose up
