import pytest
from pydantic import ValidationError
from model import Contract, User


def test_user_all_fields_correct() -> None:
    User(username="scolvin", password1="zxcvbn", password2="zxcvbn")


def test_user_passwords_dont_match() -> None:
    with pytest.raises(ValidationError):
        User(username="scolvin", password1="zxcvb2", password2="zxcvbn")


def test_user_passwords_empty() -> None:
    with pytest.raises(ValidationError):
        User(username="scolvin", password1="", password2="")


def test_user_no_username() -> None:
    with pytest.raises(ValidationError):
        User(password1="zxcvbn", password2="zxcvbn")


def test_all_fields_filled_correct() -> None:
    user = User(username="user", password1="test123", password2="test123")
    Contract(
        name="new_contract",
        type="phone bill",
        effective_date="12-12-2012",
        end_date="12-12-2020",
        renewal_state=True,
        user=user,
    )


def test_end_date_smaller_effective_date() -> None:
    user = User(username="user", password1="test123", password2="test123")
    with pytest.raises(
        ValueError, match="End date has to be later than effective date"
    ):
        Contract(
            name="new_contract",
            type="phone bill",
            effective_date="12-12-2012",
            end_date="12-12-2011",
            renewal_state=True,
            user=user,
        )


def test_user_model():
    User(username="scolvin", password1="zxcvbn", password2="zxcvbn")
