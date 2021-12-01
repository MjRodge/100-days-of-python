from coffee_recipes import MENU, resources


def take_customer_order():
    customer_selection = input("what drink? espresso/latte/cappuccino: ").lower()
    print(customer_selection)

def print_resources(current_resources):
    print(current_resources)

def make_a_coffee():
    print("coffee, yum")
    take_customer_order()
    print_resources(resources)

make_a_coffee()

