from file_io.json_io import JsonIO


class UserJson(JsonIO):
    file = "config/user.json"


class ContractJson(JsonIO):
    file = "config/contract.json"
