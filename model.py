from pydantic import BaseModel, field_validator, model_validator, SecretStr
from typing_extensions import Self
from datetime import datetime


class User(BaseModel):
    name: str

    @field_validator("name")
    def check_username(cls, val) -> None:
        if len(val.strip()) < 1:
            raise ValueError("username must contain at leat one letter")
        return val

    # password1: str
    # password2: str

    # @model_validator(mode="after")
    # def check_passwords_match(self) -> "User":
    #    pw1 = self.password1
    #    pw2 = self.password2
    #    if len(pw1.strip()) < 1:
    #        raise ValueError("password must at least contain of one letter")
    #    if pw1 is not None and pw2 is not None and pw1 != pw2:
    #        raise ValueError("passwords do not match")
    #    return self


class Contract(BaseModel):
    name: str
    type: str
    effective_date: str
    end_date: str
    renewal_state: bool
    user: User

    @model_validator(mode="after")
    def validate_end_date(self) -> Self:
        start_date = self.effective_date
        end_date = self.end_date
        if start_date:
            datetime.strptime(start_date, "%d-%m-%Y")
        if end_date:
            datetime.strptime(end_date, "%d-%m-%Y")
        if end_date is not None and start_date >= end_date:
            raise ValueError("End date has to be later than effective date")
        return self
