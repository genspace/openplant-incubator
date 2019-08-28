#!/bin/sh

#python 1_run_processing.py --img_name=20190525_153521.jpg
#python 2_run_calculation.py --img_name=20190525_153521_pcd.jpg

# Crop out the petri dish from the image
for file in data/raw/*
do
    echo "$(basename "$file")"
    python 1_run_processing.py --img_name=$(basename "$file")
done

# Crop out the plant from the previous output and calculate its size and health
for file in data/processed/*
do
    echo "$(basename "$file")"
    python 2_run_calculation.py --img_name=$(basename "$file")
done
