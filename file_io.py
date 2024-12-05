from __future__ import annotations
from typing import TYPE_CHECKING
import os
import json

if TYPE_CHECKING:
    from model import User


class UserJson:
    file = "config/user.json"

    @classmethod
    def create(cls, user: User) -> None:
        user_json = user.model_dump_json()
        if not os.path.exists(cls.file):
            with open(cls.file, mode="w") as file:
                file.write(user_json)
                return
        with open(cls.file, mode="a") as file:
            file.write(user_json)
            return


class ContractJson: ...
