from user_interaction import get_contract_data_from_user
from contract import Contract


if __name__ == "__main__":
    name, creation_date, duration, unit, cost_per_unit = get_contract_data_from_user()
    contract = Contract(
        name=name,
        creation_date=creation_date,
        duration=duration,
        duration_unit=unit,
        cost_per_unit=cost_per_unit,
    )
    print(contract)
