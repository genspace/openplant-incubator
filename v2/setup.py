#!/usr/env/bin python3

from models import schema
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/app.db', echo=True)
schema.Base.metadata.create_all(bind=engine)
