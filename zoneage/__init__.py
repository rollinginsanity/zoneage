"""Contains the Zoneage Class, the thing that makes the magic happen."""

from zoneage.config import Config

class Zoneage:

    config = ""

    def __init__(self):
        self.config = Config()


