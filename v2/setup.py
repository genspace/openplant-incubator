#!/usr/env/bin python3

import os
from models import schema
from sqlalchemy import create_engine

engine = create_engine(os.environ['CONNECTION_STRING'], echo=True)
schema.Base.metadata.create_all(bind=engine)
