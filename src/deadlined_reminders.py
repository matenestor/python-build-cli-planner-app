from abc import ABCMeta, abstractmethod
from collections.abc import Iterable


# not all methods on an Abstract Base Class need to be abstract
# however, if none are abstract, then the class itself is no longer abstract


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass
