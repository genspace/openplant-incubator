#!/usr/env/bin python3

import os
from models import schema
from sqlalchemy import create_engine
import time

connection_string = (
	"mysql+pymysql://root:"
	os.environ['OPENPLANT_DB_PASSWORD']
	"@openplant_db/openplant"
)
engine = create_engine(connection_string, echo=True)
time.sleep(30)
schema.Base.metadata.create_all(bind=engine)
