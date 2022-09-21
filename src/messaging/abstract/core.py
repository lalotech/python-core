from abc import ABC, abstractmethod
import uuid


class AbstractObserver(ABC):

    def __init__(self):
        self.uuid = uuid.uuid1()

    """
    when a message come this method is ivoke in the implementation
    """

    @abstractmethod
    def on_message(self, data):
        pass
