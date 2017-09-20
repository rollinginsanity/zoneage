"""Contains the Zoneage Class, the thing that makes the magic happen."""

from zoneage.config import Config
from zoneage.db import DB
import os
import sys

class Zoneage:

    config = ""
    db = ""

    def __init__(self):
        self.config = Config()

    def init_db(self):
        script_path = os.path.dirname(os.path.realpath(__file__))
        self.db = DB(script_path+"/../"+self.config.db_file)



