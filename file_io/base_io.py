from abc import ABC, abstractmethod


class BaseIO(ABC):

    @abstractmethod
    def create(cls, entry):
        """
        Method to create a new entry in the Database.
        """
        pass

    @abstractmethod
    def read(cls, entry):
        """
        Method to read a DB entry.
        """
        pass

    @abstractmethod
    def update(cls, entry):
        """
        Method to update a DB entry.
        """
        pass

    @abstractmethod
    def delete(cls):
        """
        Method to delete a DB entry.
        """
        pass
