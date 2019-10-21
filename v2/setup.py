#!/usr/env/bin python3

import os
from models import schema
from sqlalchemy import create_engine
import time

engine = create_engine(os.environ['CONNECTION_STRING'], echo=True)
time.sleep(30)
schema.Base.metadata.create_all(bind=engine)
