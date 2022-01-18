from coffee_recipes import MENU, resources


def take_customer_order():
    customer_selection = input("what drink? espresso/latte/cappuccino: ").lower()
    return customer_selection


def print_resources(current_resources):
    water = current_resources["water"]
    milk = current_resources["milk"]
    coffee = current_resources["coffee"]

    print(f"\nremaining resources: \nwater: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g")
    return water, milk, coffee


def resource_check(current_milk, current_water, current_coffee, milk_required, water_required, coffee_required):
    error_msg = []
    if current_milk < milk_required:
        error_msg.append("you need more milk")
        return error_msg, False
    elif current_water < water_required:
        error_msg.append("you need more water")
        return error_msg, False
    elif current_coffee < coffee_required:
        error_msg.append("you need more coffee")
        return error_msg, False
    else:
        return True


def make_a_coffee():
    print("coffee, yum")
    customer_order = take_customer_order()
    print(customer_order)
    water, milk, coffee = print_resources(resources)
    # resource_check(milk, water, coffee)


make_a_coffee()

