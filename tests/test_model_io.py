from file_io.model_io import UserJson, ContractJson
from model import User, Contract


def test_create_and_save_user() -> None:
    user = User(name="test_user", password1="password123", password2="password123")
    user_dict = user.model_dump()
    UserJson.create(user_dict)


def test_create_and_save_contract() -> None:
    user = User(name="test_user", password1="password123", password2="password123")
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