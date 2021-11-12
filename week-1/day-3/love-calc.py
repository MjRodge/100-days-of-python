# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower()+name2.lower()

true = name.count("t")
true += name.count("r")
true += name.count("u")
true += name.count("e")

love = name.count("l")
love += name.count("o")
love += name.count("v")
love += name.count("e")

percentage = int(str(true)+str(love))

if percentage < 10 and percentage > 90:
  print(f"your score is {percentage}, you go together like coke + mentos")
elif percentage > 40 and percentage < 50:
  print(f"your score is {percentage}, you are alright together")
else:
  print(f"your score is {percentage}") 
