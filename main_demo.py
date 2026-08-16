from product import Product
from inventory import Inventory
from customer import Customer
from order import Order
from payment import Payment
from receipt import Receipt
from employee import Employee
from admin import Admin

def admin_menu(admin, Inventory, employees):
    while True:
        print("\n=== Admin Menu ===")
        print("1. Add product")
        print("2. List product")
        print("3. Remove product")
        print("4. Hire Employee")
        print("5. Back to Login")

        choice = input("Enter choice: ")

        if choice == "1":
           name = input("product name: ")
           price = float(input("price: "))
           qty = int(input("quantity: "))
           category = input("category: ")
           Product = Product(name, price, qty, category)
           admin.add_product(Inventory, Product)
           print("product added successfully.")

        elif choice == "2":
            Product = Inventory.list_products()
            if not Product:
                print("NO Products available.")
            else:
                for p in Product:
                    print(p)

        elif choice == "3":
            pid = input("Employee name: ")
            admin.remove_product(Inventory, pid)
            print("product removed(if it existed).")

        elif choice == "4":
            ename = input("Employee name: ")
            erole = input("Role: ")
            emp = Employee(ename, erole)
            admin.hire_employee(employees, emp)
            print(f"Employee {ename} hired as {erole}.")

        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")


def employee_menu(employee, inventory):
    while True:
        print("\n=== Employee Menu ===")
        print("1. List products")
        print("2.Back to Login")

        choice = input("Enter choice: ")

        if choice == "1":
            Product = inventory.list_products()
            if not Product:
                print("No products available.")
            else:
                for p in Product:
                    print(p)
        elif choice == "2":
            break
        else:
            print("Invalid choice.")


def customer_menu(inventory, employees):
    cname = input("Enter customer name: ")
    customer = Customer(cname)

    while True:
        print("\n=== Customer Menu ===")
        print("1. Add item to cart")
        print("2. Checkout")
        print("3. Cancel Shopping")

        cchoice = input("Enter choice: ")

        if cchoice == "1":
            for p in inventory.list_products():
                print(p)
            pid = input("Enter product ID.")
            product = inventory.get_product(pid)
            if not product:
                print("Invalid product ID.")
                continue
            qty = int(input("Quantity: "))
            if product.is_available(qty):
                customer.add_to_cart(product, qty)
                print(f"{qty} of {product.name} added to cart.")
            else:
                print("Not enough stock.")

        elif cchoice == "2":
            if not employees:
                print("No employee available to process order.")
                break
            order = Order(customer, customer.checkout())
            emp = employees[0]
            emp.process_order(order, inventory)

            method = input("payment method (cash/card): ")
            payment = Payment(method, order.total)
            payment.process()

            receipt = Receipt(order, payment)
            receipt.print_receipt()
            break

        elif cchoice == "3":
            print("Shopping cancelled.")
            break
        else:
            print("Invalid choice.")


def main():
    inventory = Inventory()
    employee = []
    admin = Admin("SuperAdmin")

    print("=== supermarket Management System ===")
    while True:
        print("\n Login as:")
        print("1.Admin")
        print("2.Employee")
        print("3.Customer")
        print("4.Exit")

        role = input("Enter choice: ")

        if role == "1":
            admin_menu(admin, inventory, employee)
        elif role == "2":
            if not employee:
                print("No employees hired yet.")
            else:
                employee = employee[0]
                employee_menu(employee, inventory)
        elif role == "3":
            customer_menu(inventory, employee)
        elif role == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()















    