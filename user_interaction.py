from getpass import getpass


def enter_username() -> str:
    username = input("Create username: ").strip()
    if len(username) < 1:
        print("Invalid username")
        return enter_username()
    return username


def enter_password_and_validation_password() -> str:
    pw1 = getpass("Enter password: ").strip()
    pw2 = getpass("Enter password again: ").strip()

    # frontend validation
    if len(pw1) < 1 or (pw1 != pw2):
        print("Passwords empty or did not match!")
        return enter_password_and_validation_password()
    return pw1, pw2


# def get_contract_data_from_user() -> tuple[str]:
#    name = input("Enter the contract name:\n").strip()
#    creation_date = input("Enter creation date(dd-mm-yyyy):\n").strip()
#    duration_and_unit = input(
#        "Enter contract duration and unit(d|m|y) separated by a space' '.\n"
#    ).strip()
#    duration, unit = duration_and_unit.split()
#    cost_per_unit = input("Enter the cost per duration unit(Just the number): ")
#    return name, creation_date, duration, unit, cost_per_unit
