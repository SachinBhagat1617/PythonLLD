from .ObservableInterface import ObservableInterface
from Observer import ObserverInterface
class IphoneStockObservable(ObservableInterface):
    observerList=[]
    def __init__(self,quantity:int):
        self.quantity=quantity

    def addObserver(self,observer:ObserverInterface):
        return self.observerList.append(observer)
    
    def removeObserver(self,observer:ObserverInterface):
        return self.observerList.remove(observer)
    
    def getStockQuantity(self):
        return self.quantity
    
    def notifyUser(self):
        for obsv in self.observerList:
            obsv.notify()

    def setStockQuantity(self,quantity: int):
        if(self.quantity==0):
            self.quantity=quantity
            self.notifyUser()
            return
        self.quantity=quantity