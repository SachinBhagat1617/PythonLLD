from .PaymentSrategy import PaymentStrategy
class DebitCard(PaymentStrategy):
    def __init__(self,cardNo:int):
        self.cardNo=cardNo
    
    def pay(self):
        print(f"Paying from Debit Card No. {self.cardNo}")