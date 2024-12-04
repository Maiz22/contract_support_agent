from datetime import datetime


class Contract:
    def __init__(
        self,
        name: str,
        creation_date: str,
        duration: int,
        cost_per_unit: float,
        duration_unit: str,
    ) -> None:
        self.name = name
        self.creation_date = creation_date
        self.duration = duration
        self.duration_unit = duration_unit
        self.cost_per_unit = cost_per_unit

    @property
    def creation_date(self) -> str:
        """creation_date getter"""
        return self._creation_date

    @creation_date.setter
    def creation_date(self, date) -> None:
        """
        Creation date setter.
        Sets create_date as a datetime object.
        Raises a ValueError if format does not match.
        """
        format = "%d-%m-%Y"
        self._creation_date = datetime.strptime(date, format)

    @property
    def duration_unit(self) -> str:
        """duration_unit getter"""
        return self._duration_unit

    @duration_unit.setter
    def duration_unit(self, unit) -> str:
        """
        duration_unit setter.
        Sets the duration_unit if a valid unit is given.
        Raises a ValueError if not.
        """
        valid_units = set(["d", "w", "m"])
        if unit not in valid_units:
            raise ValueError("Invalid duration unit")
        self._duration_unit = unit

    def __str__(self) -> str:
        return "\nContract Data:\nName: {}\nCreation Date: {}\nDuration: {}\nDuration Unit{}\nCost Per Unit: {}".format(
            self.name,
            self.creation_date,
            self.duration,
            self.duration_unit,
            self.cost_per_unit,
        )
