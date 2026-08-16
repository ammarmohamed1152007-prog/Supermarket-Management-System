from utils import IDGenerator


class Payment:
    def __init__(self, method, amount):
        self.id = IDGenerator.generate_id("pay")
        self.method = method
        self.amount = amount
        self.status = "INIT"

    def process(self):
        if self.amount > 0:
            self.status = "SUCCESS"
        else:
            self.status = "FAILED"

        return self.status
