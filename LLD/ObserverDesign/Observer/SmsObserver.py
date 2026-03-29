from .ObserverInterface import ObserverInterface
from Observable.IphoneStockObservable import ObservableInterface
class SmsObserver(ObserverInterface):
    def __init__(self, phoneNo:int, observable:ObservableInterface):
        self.phoneNo=phoneNo
        self.observable=observable

    def notify(self):
        print(f"Sending mail to {self.phoneNo}")
        print(f"Product is back {self.observable.getStockQuantity()}")