def add (x, y):
  return x + y

def subtract (x, y):
  return x - y

def multiply (x, y):
  return x * y

def divide (x, y):
  return x / y

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

num1 = float(input("what is first number?: "))
for op in operations:
  print(op)
more_calcs = True

while more_calcs == True:
  op_symbol = input("pick an operator from the list above: ")
  num2 = float(input("what is the next number?: "))
  calc_func = operations[op_symbol]
  answer = calc_func(num1, num2)
  print(f"{num1} {op_symbol} {num2} = {answer}")
  calc_continue = input("would you like to do additional calculations? (y or n): ")
  if calc_continue == "y":
    more_calcs = True
    num1 = answer
  else:
    more_calcs = False
    



