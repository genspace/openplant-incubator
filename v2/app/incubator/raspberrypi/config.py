DEFAULT_CONFIG_PARAMS = {
    # Edit these for the particular incubator
    "pictures_folder": "/root/pictures",
    # This is the folder inside our S3 bucket.
    "incubator_name": None,
    # How often to take pictures / log to database
    "sleep_interval_sec": 300,
    # Time range for lights on / off
    "light_time": (800, 2399),
    # S3 Credentials
    "aws_access_key_id": None,
    "aws_secret_access_key": None
}
