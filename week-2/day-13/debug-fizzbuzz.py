#lines 6 and 8 were if statements, changed to elif to fix bug of multiple prints for same number if divisible by both 3 and 5
#changed line 4 if statement to and, instead of or
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])