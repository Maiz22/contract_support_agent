from user_interaction import *
from model import User
import sys


def parse_argvs(args) -> None:
    new_user = False
    if args[0] == "new":
        new_user = True
    return new_user


if __name__ == "__main__":
    new_user = parse_argvs(sys.argv)
    last_user = None
    if new_user or last_user is None:
        username = enter_username()
        password1, password2 = enter_password_and_validation_password()
    user = User(username=username, password1=password1, password2=password2)
    print(user)
