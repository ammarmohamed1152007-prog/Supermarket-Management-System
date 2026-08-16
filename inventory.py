class Inventory:
    def __init__(self):
        self.product = {}

    def add_product(self, product):
        self.product[product.id] = product

    def remove_product(self, product_id):
        if product_id in self.product:
            del self.product[product_id]

    def get_product(self, product_id):
        return self.product.get(product_id, None)

    def list_products(self):
        return list(self.product.values())

    def check_availability(self, product_id, amount=1):
        product = self.get_product(product_id)
        return product and product.is_available(amount)            