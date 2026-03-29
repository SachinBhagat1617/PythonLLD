from abc import ABC, abstractmethod
from Observer import ObserverInterface
class ObservableInterface:
    @abstractmethod
    def addObserver(observer:ObserverInterface):
        pass

    @abstractmethod
    def removeObserver(observer:ObserverInterface):
        pass

    @abstractmethod
    def getStockQuantity():
        pass

    @abstractmethod
    def notifyUser():
        pass

    @abstractmethod
    def setStockQuantity():
        pass