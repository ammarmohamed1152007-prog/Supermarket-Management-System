from utils import IDGenerator

class Order:
    def __init__(self, customer, items):
        self.id = IDGenerator.generate_id("ord")
        self.customer = customer
        self.items = items.copy() 
        self.status = "PENDING"
        self.total = sum(p.price * q for p, q in items.items())

    def mark_paid(self):
        self.status = "PAID"

    def __str__(self):
        return f"Order {self.id} ({self.status}) - Total: {self.total}"