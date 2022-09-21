from .abstract.core import AbstractObserver
from .model.core import MessageData


class MessageManager:

    def __init__(self):
        print("build the MessageManager")
        self._observers = dict()  # map to keep all the observers

    '''
    subscribe()
    - observer:AbstractObserver - the Observer instance to add
    - channel:string -  the 'string' channel representation
    '''
    def subscribe(self, observer: AbstractObserver, channel="generic"):
       
        self.___check_if_channel_exists(channel)
       
        observer_list = self._observers[channel]
        observer_list.append(observer)

    '''
    publish()
    - data: MessageData - 
    - channel:string - the bus name to publish or use the generic
    '''
    def publish(self, data: MessageData, channel='generic'):
        print("message in channel {}".format(channel))
        self.___check_if_channel_exists()

        for observer in self._observers[channel]:
            observer.on_message(data)

    def topics(self):
        channels = [key for key in self._observers]
        print(f'topics: {channels}')
        return len(channels)

    def observers(self):
        print("see the topics list {0}".format(len(self._observers)))
        return len(self._observers)

    '''
    private methods
    '''    
    def __print_topic(self, key):
        print(key)
        print(self._observers[key])
    
    def ___check_if_channel_exists(self, channel='generic'):
         if not channel in self._observers:
            self._observers[channel] = list()
