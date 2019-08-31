#!/bin/sh

mkdir data
# An example of copying files for a certain date from s3: date +%Y-%m-%d
aws s3 cp s3://BUCKET/ folder --exclude "*" --include "2015-08-15*" --recursive

for file in data/*
do
    python process_all.py --img_name=$(basename "$file")
done

rm -rf data/
