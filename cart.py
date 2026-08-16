class Cart :
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def clear(self):
        self.items.clear()

    def calculate_total(self):
        return sum(p.price * q for p, q in self.items.items())           