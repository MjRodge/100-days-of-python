from prettytable import PrettyTable

my_table = PrettyTable()

my_table.add_column("pokemon name", ["bulbasaur", "squirtle", "charmander"])
my_table.add_column("type", ["grass", "water", "fire"])

my_table.align = "l"

print(my_table)