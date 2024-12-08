from __future__ import annotations
from typing import TYPE_CHECKING
import os
import json
from file_io.base_io import BaseIO


class JsonIO(BaseIO):
    """
    Base class to interact with a json DB using CRUD methods.
    """

    file = None
    unique_keys: list = []

    # missing logic for when json_data file does not exists already
    @classmethod
    def create(cls, entry: dict) -> None:
        """
        Takes a python dictionary as entry, creates a new json
        file, if no file exists already, and dumps the entry into
        it.
        If a json file already exists, the entry will be appended
        to it.
        """

        # check if a file path has been added to the concrete implmentation
        if cls.file is None:
            raise ValueError(
                "File is None. Please add a file path in your implementation"
            )

        # create a new JSON file and add one entry if it does not exists already
        if not os.path.exists(cls.file):
            with open(cls.file, mode="w") as file:
                if isinstance(entry, dict):
                    entry_list = [entry]
                json.dump(entry_list, file, indent=4)
                file.close()
                return

        # get data from json and check if defined entries are unique
        with open(cls.file, mode="r") as file:
            entry_list = json.load(file)
            if len(cls.unique_keys) > 0:
                for key in cls.unique_keys:
                    for element in entry_list:
                        if element[key] == entry[key]:
                            raise ValueError("Unique key already exists in JSON")
            if not isinstance(entry_list, list):
                raise TypeError("Parsed JSON should be of type list")
            file.close()

        # validate entry and add it to the list to save it inside the JSON.
        with open(cls.file, mode="w") as file:
            if not isinstance(entry, dict):
                raise TypeError("Entry should be a dictionary")
            entry_list.append(entry)
            json.dump(entry_list, file, indent=4)
            file.close()
            return
