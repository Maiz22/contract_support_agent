import pytest
from contract import Contract
import re


def test_contract_all_valid_parameters() -> None:
    new_contract = Contract(
        name="test contract",
        creation_date="22-12-2022",
        duration="12",
        duration_unit="m",
        cost_per_unit=19.99,
    )
    assert isinstance(new_contract, Contract)


def test_invalid_creation_date() -> None:
    with pytest.raises(
        ValueError, match="time data '22.12.2022' does not match format '%d-%m-%Y'"
    ):
        new_contract = Contract(
            name="test contract",
            creation_date="22.12.2022",
            duration="12",
            duration_unit="m",
            cost_per_unit=19.99,
        )


def test_invalid_duration_unit() -> None:
    with pytest.raises(ValueError, match="Invalid duration unit"):
        new_contract = Contract(
            name="test contract",
            creation_date="22-12-2022",
            duration="12",
            duration_unit="month",
            cost_per_unit=19.99,
        )


def test_contract_no_duration_unit() -> None:
    with pytest.raises(
        TypeError,
        match=re.escape(
            "Contract.__init__() missing 1 required positional argument: 'duration_unit'"
        ),
    ):
        new_contract = Contract(
            name="test contract",
            creation_date="22-12-2022",
            duration="12",
            cost_per_unit=19.99,
        )


def test_contract_missing_name() -> None:
    with pytest.raises(
        TypeError,
        match=re.escape(
            "Contract.__init__() missing 1 required positional argument: 'name'"
        ),
    ):
        new_contract = Contract(
            creation_date="22-12-2022",
            duration="12",
            cost_per_unit=19.99,
            duration_unit="m",
        )
