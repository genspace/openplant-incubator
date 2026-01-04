DEFAULT_CONFIG_PARAMS = {
    # Edit these for the particular incubator
    "pictures_folder": "/home/pi/pictures",
    # This is the folder inside our S3 bucket.
    "incubator_name": None,
    # How often to take pictures
    "camera_freq_seconds": 60 ** 2 * 2,
    # How often to log temp reading
    "sensor_freq_seconds": 60 * 10,
    # Time range for lights on / off
    "light_time": "800,2399",
    # Resolution for camera
    "camera_resolution": "1280,720"
}
