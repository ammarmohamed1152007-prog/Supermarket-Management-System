```mermaid
classDiagram
    class Admin {
        +id
        +name
        +add_product()
        +remove_product()
        +hire_employee()
    }

    class Employee {
        +id
        +name
        +role
        +process_order()
    }

    class Customer {
        +id
        +name
        +cart
        +add_to_cart()
        +checkout()
    }

    class Product {
        +id
        +name
        +price
        +quantity
        +category
        +update_stock()
        +is_available()
    }

    class Inventory {
        +products
        +add_product()
        +remove_product()
        +get_product()
        +list_products()
        +check_availability()
    }

    class Cart {
        +items
        +add_item()
        +clear()
        +calculate_total()
    }

    class Order {
        +id
        +customer
        +items
        +status
        +total
        +mark_paid()
    }

    class Payment {
        +id
        +method
        +amount
        +status
        +process()
    }

    class Receipt {
        +order
        +payment
        +print_receipt()
    }

    class Utils {
        +generate_id()
    }

    %% Relationships
    Admin --> Inventory
    Admin --> Employee
    Employee --> Order
    Customer --> Cart
    Cart --> Product
    Order --> Customer
    Order --> Product
    Payment --> Order
    Receipt --> Order
    Receipt --> Payment
    Inventory --> Product
