from utils import IDGenerator

class Product:
    def __init__(self, name, price, quantity, category=None):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

        def update_stock(self, delta):
            self.quantity += delta

        def is_available(self, amount=1):
            return self.quantity >= amount

        def __str__(self):
            return f"{self.id}: {self.name} (price: {self.price}, stock: {self.quantity})"
        
