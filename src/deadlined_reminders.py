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

    @classmethod
    def __subclasshook__(cls, subclass):
        """A class, that passes this check, is considered "a virtual subclass"
        of this class. E.g. 'external_reminders.EveningReminder` is a
        virtual subclass of a 'deadlined_reminders.DeadlinedReminder'.

        From the project tutorial:
          This class method is called as part of
          issubclass(ReminderClass, DeadlinedReminder).
          It checks that the given subclass contains the required methods
          __iter__() and is_due() anywhere in its hierarchy. If they are
          present, the class is considered to be a virtual subclass of the
          DeadlinedReminder.

        """
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any(
                attr in SuperClass.__dict__ for SuperClass in subclass.__mro__
            )

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True



class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text

    def is_due(self):
        return self.date <= datetime.now()

    def __iter__(self):
        return iter([self.text, self.date.isoformat()])

