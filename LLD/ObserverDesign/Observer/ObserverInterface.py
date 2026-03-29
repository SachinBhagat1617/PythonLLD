from abc import ABC, abstractmethod

class ObserverInterface:
    @abstractmethod
    def notify():
        pass