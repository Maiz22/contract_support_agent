def get_contract_data_from_user() -> tuple[str]:
    name = input("Enter the contract name:\n").strip()
    creation_date = input("Enter creation date(dd-mm-yyyy):\n").strip()
    duration_and_unit = input(
        "Enter contract duration and unit(d|m|y) separated by a space' '.\n"
    ).strip()
    duration, unit = duration_and_unit.split()
    cost_per_unit = input("Enter the cost per duration unit(Just the number): ")
    return name, creation_date, duration, unit, cost_per_unit
