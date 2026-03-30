from Toppings.ExtraCheese import ExtraCheese
from Toppings.ExtraVeggie import ExtraVeggie
from basePizza.CheesyPizza import ChessyPizza
from basePizza.BasePizza import BasePizza
pizza1:BasePizza=ExtraCheese(ExtraVeggie(ChessyPizza))
print(pizza1.getCost())
print(pizza1.getDescription())