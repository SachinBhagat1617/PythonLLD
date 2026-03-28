from cart.ShoppingCart import ShoppingCart
from payment.CreditCard import CreditCard


cart:ShoppingCart=ShoppingCart(CreditCard(123456789))
cart.checkout()