"""Class containing exceptions. Yes, I like to write my own."""

class MissingConfigFileException(Exception):
    """Raise when the config file is missing."""

class InvalidConfigFormatFoundException(Exception):
    """The config file is not valid JSON."""

class MissingConfigElementException(Exception):
    """The config file is missing a setting."""

