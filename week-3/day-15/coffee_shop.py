from coffee_recipes import MENU


def take_customer_order():
    customer_selection = input("what drink? espresso/latte/cappuccino: ").lower()
    print(customer_selection)

def make_a_coffee():
    print("coffee, yum")
    take_customer_order()

make_a_coffee()

