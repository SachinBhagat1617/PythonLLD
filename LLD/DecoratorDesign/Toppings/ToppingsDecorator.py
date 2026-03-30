from basePizza.BasePizza import BasePizza

class ToppingsDecorator(BasePizza): # ToppingDecorator with topings and BasePizza is a Pizza
    def __init__(self,basePizza:BasePizza):
        self.basePizza=basePizza