# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
num_of_guests = len(names)
gunshot = random.randint(0, num_of_guests-1)
payer = names[gunshot]
print(f"{payer} is going to buy the meal today.")
