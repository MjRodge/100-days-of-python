#Write your code below this row 👇
for x in range(1, 101):
  if x % 5 == 0 and x % 3 == 0:
    print("fizzbuzz")
  elif x % 5 == 0:
    print("buzz")
  elif x % 3 == 0:
    print("fizz")
  else:
    print(x)