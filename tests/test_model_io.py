from file_io.model_io import UserJson, ContractJson
from model import User, Contract
import pytest


def test_create_and_save_user() -> None:
    user = User(name="test_user")
    user_dict = user.model_dump()
    UserJson.create(user_dict)


def test_create_and_save_contract() -> None:
    user = User(name="test_user")
    contract = Contract(
        name="phone contract",
        type="phone contract",
        effective_date="12-12-2022",
        end_date="12-12-2024",
        renewal_state=True,
        user=user,
    )
    contract_dict = contract.model_dump()
    ContractJson.create(contract_dict)


def test_create_user_and_save_in_db() -> None:
    user = User(name="scolvin")
    user_dict = user.model_dump()
    UserJson.create(user_dict)


def test_user_already_exists() -> None:
    with pytest.raises(ValueError, match="Unique key already exists in JSON"):
        user = User(name="scolvin")
        user_dict = user.model_dump()
        UserJson.create(user_dict)


def test_delete_user_by_name() -> None:
    UserJson.delete(key="name", val="test_user")
