# Import libraries
import json
import logging


# Functions
def if_json_file_name(variable) -> bool:
    """Check if variable is a json file"""
    try:
        if ".json" in variable[-5:]:
            return True
    except Exception as e:
        logging.error(f"Error while checking if json file name: {e}")
    return False


def get_json_object(json_file: str) -> dict:
    """
    Get json object from json file
    :param json_file:      name of json file containing job details
    """
    try:
        with open(json_file) as jf:
            json_object = json.load(jf)
            return json_object
    except FileNotFoundError:
        logging.error(f"JSON file '{json_file}' not found.")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file '{json_file}'. Check JSON syntax.")
    except Exception as e:
        logging.error(f"Error while getting json object: {e}")
    return {}


def handle_data_from_front_end(from_front_end) -> dict:
    """Handle data from front end side"""
    try:
        if type(from_front_end) is str:
            if if_json_file_name(from_front_end):
                json_object = get_json_object(from_front_end)
            else:
                return {}
        else:
            json_object = from_front_end
        return json_object
    except Exception as e:
        logging.error(f"Error while handling the data from front end: {e}")
        return {}
