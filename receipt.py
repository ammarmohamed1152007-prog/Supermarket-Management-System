class Receipt:
    def __init__(self, order, payment):
        self.order = order
        self.payment = payment
    def print_receipt(self):
        print("=====RECEIPT=====")
        print(f"Order ID: {self.order.id}")
        print(f"Customer: {self.order.customer.name}")
        print("\nItems:")

        for product, quantity in self.order.cart.items.items():
            print(f"{product.name} x {quantity} = {product.price * quantity}")
        print(f"\nTotal: {self.order.total}")    
        print(f"Payment: {self.payment.method} ({self.payment.status})")
        

            