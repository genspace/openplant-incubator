#!/usr/env/bin python

import os

def get_connection_string():
    components = [
        os.environ['DB_DRIVER'], '://',
        os.environ['DB_USER'], ':',
        os.environ['DB_PASSWORD'], '@',
        os.environ['DB_CONTAINER'], '/',
        os.environ['DB_NAME']
    ]
    connection_string = ''.join(components)
    return connection_string
