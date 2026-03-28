from .PaymentSrategy import PaymentStrategy
class CreditCard(PaymentStrategy):
    def __init__(self,cardNo:int):
        self.cardNo=cardNo
    
    def pay(self):
        print(f"Paying from Credit Card No. {self.cardNo}")