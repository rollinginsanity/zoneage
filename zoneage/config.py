"""This module includes the Config class, which holds the config loaded from a config file."""
import json
from zoneage.exceptions import MissingConfigFileException, InvalidConfigFormatFoundException, MissingConfigElementException
import pkg_resources # used to load meta-config-format file.

class Config:
    config_file = ""

    # Some of the items from this dict will get set in their own variables.
    # If additional settings are thrown in to the config file, they will still be accessible here.
    config_settings = {}


    def __init__(self):
        """Constructor, doesn't do anything. Here in case I need it later. Probably unpythonic."""

    def load_config(self, config_file):
        """Loads a config file and parses it.

        :param config_file: A path to the config file. See the config file spec (when I write one).
        :return:
        """

        print("CONFIG: Loading config file "+config_file+".")

        # Loads the file containing the config. If the file doesn't exist, it errors and an exception is raised.
        try:
            self.config_file = open(config_file)
        except Exception as e:
            raise MissingConfigFileException("No config file with that name found.")

        print("CONFIG: Config file "+config_file+" loaded.")

        print("CONFIG: Parsing "+config_file+" as json.")

        # The config file is then parsed (it should be JSON). If parsing fails, raise an exception.
        try:
            self.config_settings = json.load(self.config_file)
        except Exception as e:
            raise InvalidConfigFormatFoundException("Invalid config file format. Please ensure it is valid JSON.")

        print("CONFIG: Config file parsed and loaded.")

        # Now validate the config. I split this out in to a different function.

        self.validate_config()

    def validate_config(self):
        """
        Validates the elements in the config file against the config-format file. Overkill = yes.

        :return:
        """
        print("CONFIG: Validating the config against expected settings.")
        # Load the config-format file using the pkg_resources module. This is apparently the proper way to do things.
        try:

            # A note on the below. The resource_stream function returns binary, so I decode it as a utf8 string.
            # There is a resource_string option, couldn't figure it out.
            config_format = json.loads(pkg_resources.resource_stream("zoneage", "/meta/config-format.json").read().decode("utf8"))
        except Exception as e:
            raise Exception("Internal package config is broken. Consider re-installing or re-evaluate life choices.")

        print("CONFIG: Loaded the config format file.")

        # Loop through the required config elements in the format file and check if they are there in the actual config file.

        for config_element in config_format["config_elements"]:
            #Assume the element isn't there.
            element_exists = False

            # The value from the config file.
            config_file_value = ""

            ### Check an element with the correct name exists.

            print("CONFIG: Checking for parameter '"+config_element["name"]+"' in config file.")
            print("CONFIG: Mandatory element - "+str(config_element["mandatory"]))

            for key, value in self.config_settings.items():
                if key == config_element["name"]:
                    element_exists = True
                    config_file_value = value
                    print("Value: "+config_file_value)

            if not element_exists and config_element["mandatory"]:
                raise MissingConfigElementException("Parameter "+config_element["name"]+" missing from the config file.")

            if not element_exists:
                print("CONFIG: Optional parameter "+config_element["name"]+" not found.")

            # And now set the item as a property on the config class.
            setattr(self,config_element["name"], config_file_value)





