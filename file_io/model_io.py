"""
For every model that you want to user to save data
in a json, you can create a separate class that inheritates
from JsonIO. Specify the file (rel path). All basic DB 
functionalities can be inherited from Json IO.
"""

from file_io.json_io import JsonIO


class UserJson(JsonIO):
    file = "config/user.json"


class ContractJson(JsonIO):
    file = "config/contract.json"
