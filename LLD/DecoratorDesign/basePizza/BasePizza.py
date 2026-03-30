from abc import ABC,abstractmethod

class BasePizza:
    @abstractmethod
    def getCost()->int:
        pass

    @abstractmethod
    def getDescription()->str:
        pass