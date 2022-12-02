from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable
from datetime import datetime

from dateutil.parser import parse


# not all methods on an Abstract Base Class need to be abstract,
# however, if none are abstract, then the class itself is no longer abstract
# NOTE: not used during the project, it is just a showcase
class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass


# since python 3.4 you can also create an Abstract Base Class
# by inheriting from the ABC class of the abc module
class DeadlinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self):
        pass


class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

