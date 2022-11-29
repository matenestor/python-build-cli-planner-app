from abc import ABC, ABCMeta, abstractmethod
from collections.abc import Iterable


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

