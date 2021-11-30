############DEBUGGING#####################

# # Describe Problem
#my_function() takes a range of numbers, loops through them, and prints "you got it" when i == 20.
#however, no message is ever printed to console
#(upper bound of range() is ommitted, 20 is never the value of i)
#test assumptions
####
#def my_function():
#  for i in range(1, 20):
#    if i == 20:
#      print("You got it")
#my_function()
####

# # Reproduce the Bug
#occassionally, the error "IndexError: list index out of range" is thrown, while sometimes the die number is returned correctly
#the randint(1,6) line should be randint(0, len(dice_imgs)-1) to ensure always in range 
####
#from random import randint
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, len(dice_imgs)-1)
#print(dice_imgs[dice_num])
####

# # Play Computer
#input of 1994 causes error
#this is because there is no equal to 1994 comparator
#elif year >= 1994: print("gen z.")
####
#year = int(input("What's your year of birth?"))
#if year > 1980 and year < 1994:
#  print("You are a millenial.")
#elif year >= 1994:
#  print("You are a Gen Z.")
####

# # Fix the Errors
#age is a string, needs to be type converted to int
####
# age = int(input("How old are you?"))
# if age > 18:
# print(f"You can drive at age {age}.")
####

# #Print is Your Friend
#int input for word_per_page is a comparator (==) instead of assignment
####
#ages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)
####

# #Use a Debugger
#stepped through function below using thonny
#indentation list on b_list.appent(new_item) line, needs to be within the scope of for loop
####
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
####