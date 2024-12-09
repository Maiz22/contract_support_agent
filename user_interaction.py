from getpass import getpass


def enter_username() -> str:
    username = input("Create username: ").strip()
    if len(username) < 1:
        print("Invalid username")
        return enter_username()
    return username


# def enter_password_and_validation_password() -> str:
#    pw1 = getpass("Enter password: ").strip()
#    pw2 = getpass("Enter password again: ").strip()
#
#    # frontend validation
#    if len(pw1) < 1 or (pw1 != pw2):
#        print("Passwords empty or did not match!")
#        return enter_password_and_validation_password()
#    return pw1, pw2
