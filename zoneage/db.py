"""
This module holds the DB class for interacting with the database.

Mostly responsible for explosing the SQLAlchemy declarative_base object, and creating the DB with the correct schema.
"""
import os
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB:
    base = declarative_base()
    session = ""
    engine = ""

    def __init__(self, path):
        """
        Creates the bits and pieces the DB stuff needs.
        :param path: The path to the DB file.
        """

        #T he SQLAlchemy engine object.
        self.engine = create_engine('sqlite:///' + path)

        # If the DB file doesn't exist, create one.
        if not os.path.isfile(path):

            print("DB: Creating DB file at: "+path)

            # We import the models here. We need to so the schema gets dumped in the DB.
            import zoneage.models
            self.base.metadata.create_all(self.engine)

        else:
            print("DB: DB Already Exists. Using existing DB located at: "+path)

        #Create a session object so we can do something with the DB.
        session = sessionmaker(bind=self.engine)
        self.session = session()