#!/usr/env/bin python3

"""
Main schema file
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, ForeignKey, String, Integer, Float, DateTime, JSON, Date
)


Base = declarative_base()


class Sample(Base):
    __tablename__ = 'plant'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    experiment_id = Column(Integer, ForeignKey('experiment.id'))
    barcode = Column(Integer, unique=True)
    metadata = Column(JSON)
    notes = Column(JSON)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Experiment(Base):
    __tablename__ = 'experiment'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    control_id = Column(Integer, ForeignKey('experiment.id'))
    plasmid_id = Column(Integer, ForeignKey('plasmid.id'))
    description = Column(String)
    date_initiated = Column(Date)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class RawImage(Base):
    __tablename__ = 'raw_image'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    incubator_id = Column(Integer, ForeignKey('incubator.id'))
    time = Column(DateTime)
    s3_filepath = Column(String(500))


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    raw_image_id = Column(Integer, ForeignKey('raw_image.id'))
    processing_method = Column(String(500))
    plant_id = Column(Integer, ForeignKey('plant.id'))
    s3_filepath = Column(String(500))


class Analysis(Base):
    __tablename__ = 'analysis'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    image_id = Column(Integer, ForeignKey('image.id'))
    size = Column(Float)
    health = Column(Float)


class Sensor(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True, autoincrement=True,)
    incubator_id = Column(Integer, ForeignKey('incubator.id'))
    time = Column(DateTime)
    temperature = Column(Float)
    humidity = Column(Float)
    light = Column(Integer)

    def __repr__(self):
        return (("<Sensor(id=%s, incubator_id=%s, "
                "time=%s, temperature=%s, "
                "humidity=%s, light=%s)>") %
                (self.id, self.incubator_id,
                 self.time, self.temperature,
                 self.humidity, self.light))


class Incubator(Base):
    __tablename__ = 'incubator'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    number = Column(Integer, unique=True)


class Plasmid(Base):
    __tablename__ = 'plasmid'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    name = Column(String, unique=True)
    metadata = Column(JSON)
