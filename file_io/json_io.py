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

    @classmethod
    def create(cls, entry: dict) -> None:
        """
        Takes a python dictionary as entry, creates a new json
        file, if no file exists already, and dumps the entry into
        it.
        If a json file already exists, the entry will be appended
        to it.
        """
        if cls.file is None:
            raise ValueError(
                "File is None. Please add a file path in your implementation"
            )
        if not os.path.exists(cls.file):
            with open(cls.file, mode="w") as file:
                if isinstance(entry, dict):
                    entry_list = [entry]
                json.dump(entry_list, file, indent=4)
                file.close()
        with open(cls.file, mode="r") as file:
            entry_list = json.load(file)
            if not isinstance(entry_list, list):
                raise TypeError("Parsed JSON should be of type list")
            file.close()
        with open(cls.file, mode="w") as file:
            if not isinstance(entry, dict):
                raise TypeError("Entry should be a dictionary")
            entry_list.append(entry)
            json.dump(entry_list, file, indent=4)
            file.close()
