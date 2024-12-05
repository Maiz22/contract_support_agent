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
        user_dict = user.model_dump()
        user_list = [user_dict]
        if not os.path.exists(cls.file):
            with open(cls.file, mode="w") as file:
                json.dump(user_list, file, indent=4)
                file.close()
                return
        with open(cls.file, mode="r") as file:
            user_list = json.load(file)
            file.close()
        with open(cls.file, mode="w") as file:
            user_list.append(user.model_dump())
            json.dump(user_list, file, indent=4)
            file.close()


class ContractJson: ...
