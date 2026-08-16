from utils import IDGenerator
from cart import Cart

class Customer:
    def __init__(self, name):
        self.name = name
        self.id = IDGenerator.generate_id("cust")
        self.cart = Cart()

    def add_to_cart(self, product, quantity=1):
        self.cart.add_item(product, quantity)
    def checkout(self):
        return self.cart.items    