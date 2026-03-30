from .ToppingsDecorator import ToppingsDecorator
from basePizza.BasePizza import BasePizza
class ExtraChicken(ToppingsDecorator):
    def __init__(self,basePizza:BasePizza):
        self.basePizza=basePizza

    def getCost(self)->int:
        return self.basePizza.getCost()+30
    def getDescription(self)->str:
        return self.basePizza.getDescription()+" Extra Chicken"