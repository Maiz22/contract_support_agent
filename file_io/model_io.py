"""
For every model that you want to user to save data
in a json, you can create a separate class that inheritates
from JsonIO. Specify the file (rel path). All basic DB 
functionalities can be inherited from Json IO.
"""

from file_io.json_io import JsonIO


# currently file must be in json_data
class UserJson(JsonIO):
    file = "json_data/user.json"
    unique_keys = ["name"]


# currently file must be in json_data
class ContractJson(JsonIO):
    file = "json_data/contract.json"
