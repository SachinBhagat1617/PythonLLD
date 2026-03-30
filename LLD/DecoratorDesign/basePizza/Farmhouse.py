from .BasePizza import BasePizza
class Farmhouse(BasePizza):
    def getCost()->int:
        return 210
    def getDescription()->str:
        return "FarmHouse Pizza"