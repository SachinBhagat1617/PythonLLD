from .ObserverInterface import ObserverInterface
from Observable.IphoneStockObservable import ObservableInterface
class EmailObserver(ObserverInterface):
    def __init__(self,emailId: str, observable: ObservableInterface):
        self.emailId=emailId
        self.observable=observable
    def notify(self):
        print(f"Sending mail to {self.emailId}")
        print(f"Product is back {self.observable.getStockQuantity()}")
