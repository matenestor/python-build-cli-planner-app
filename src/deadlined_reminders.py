from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable

from dateutil.parser import parse


# - not all methods on an Abstract Base Class need to be abstract,
#   however, if none are abstract, then the class itself is no longer abstract
# - since python 3.4 you can also create an Abstract Base Class by inheriting
#   from the ABC class of the abc module


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass


class DeadlinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

