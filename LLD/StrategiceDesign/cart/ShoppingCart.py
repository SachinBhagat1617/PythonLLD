from payment.PaymentSrategy import PaymentStrategy
class ShoppingCart:
    def __init__(self,paymentStrategy:PaymentStrategy):
        self.paymentStrategy=paymentStrategy

    def checkout(self):
        self.paymentStrategy.pay()