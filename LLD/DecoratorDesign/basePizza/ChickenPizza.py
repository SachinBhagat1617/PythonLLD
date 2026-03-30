from .BasePizza import BasePizza
class ChickenPizza(BasePizza):
    def getCost()->int:
        return 250
    def getDescription()->str:
        return "Chicken Pizza"