from utils import IDGenerator

class Admin :
    def __init__(self, name):
        self.name = name
        self.id = IDGenerator.generate_id("adm")

    def add_product(self , inventory, product):
        inventory.add_product(product)

    def remove_product(self , inventory, product_id):
        inventory.remove_product(product_id)

    def hire_employee(self, employees, employee):
        employees.append(employee)        
