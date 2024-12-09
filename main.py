from user_interaction import *
from model import User
import sys
from file_io.model_io import UserJson


def determine_user_action(args) -> None | User:
    """
    Takes the command line args an determines the user action
    depending on them.
    Returns the user or None.
    """
    user = None
    if args[1].lower() == "--create":
        user = create_user(username=args[2])
    elif args[1].lower() == "--delete":
        delete_user(args[2])
    elif args[1].lower() == "--help":
        print_help()
    else:
        user = get_user(args[1])
    return user


def create_user(username: str) -> None:
    """
    Takes a username, creates a User instance parses it to a
    dict like string and saves the user in the UserJson.
    """
    user = User(name=username)
    user_dict = user.model_dump()
    try:
        UserJson.create(user_dict)
        print(f"User {user.name} has been added to the JSON")
        return user
    except Exception as err:
        print(err)


def delete_user(username: str) -> None:
    """
    Takes a username and removes the user from UserJson, if
    it exists.
    """
    try:
        UserJson.delete(key="name", val=username)
        print(f"User {username} has been deleted from JSON")
    except ValueError:
        print(f"User {username} does not exists in DB.")


def get_user(username: str) -> None:
    pass


def print_help() -> None:
    print(
        """

    Valid Commands:

    --create <username> : create user with name <username>
    --delete <username> : delete user with name <username>
    <username> : login user <username>

    """
    )


if __name__ == "__main__":
    user = determine_user_action(sys.argv)
    print(user)
