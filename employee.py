from utils import IDGenerator

class Employee:
    def __init__(self, name, role="cashier"):
        self.id = IDGenerator.generate_id("emp")
        self.name = name
        self.role = role

    def process_order(self, order, inventory):
        for product, qty in order.items.items():
            if not inventory.check_availability(product.id, qty):
                raise Exception (f"{product.name} not available")
        for product, qty in order.items.items():
            product.update_stock(-qty)
        order.mark_paid()
        return True