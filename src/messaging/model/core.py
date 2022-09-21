from enum import Enum
import uuid

class MessageData:
    uuid = None
    type = None
    payload = None
    def __init__(self) -> None:
        self.uuid = uuid.uuid1()

class MessageType(Enum):
    MY_TYPE_1 = 1
    MY_TYPE_2 = 2
    MY_TYPE_3 = 3