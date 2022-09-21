from src.messaging.abstract.core import AbstractObserver
from src.messaging.model.core import MessageData, MessageType
from src.messaging.message import MessageManager
from unittest import TestCase


class MyObserver(AbstractObserver):

    def on_message(self, data):
        console = """
        on message for TestObserver: {0}
        with type {1} and
        a payload:{2}
        """.format(self.uuid, data.type, data.payload)
        print(console)


class TestObserverCase(TestCase):

    def test_main_observer(self):

        # give
        message_manager = MessageManager()
        test_observer1 = MyObserver()
        test_observer2 = MyObserver()

        message_manager.subscribe(test_observer1, "my_channel")
        message_manager.subscribe(test_observer2)
        message_manager.topics()

        message = MessageData()
        message.type = MessageType.MY_TYPE_1
        message.payload = "{\"name\":\"name1\"}"

        # when
        message_manager.publish(message)  # default bus/channel
        message_manager.publish(message, "generic")
        message_manager.publish(message, "my_channel")

        # then
        self.assertTrue(message_manager.observers() == 2)
        self.assertTrue(message_manager.topics() == 2)
        self.assertTrue(test_observer1.uuid != test_observer2.uuid)
