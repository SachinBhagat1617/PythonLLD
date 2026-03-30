from .BasePizza import BasePizza
class ChessyPizza(BasePizza):
    def getCost()->int:
        return 150
    def getDescription()->str:
        return "Chessy Pizza"