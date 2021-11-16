rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
if choice == 0:
  if comp_choice == 0:
    print(f"your choice is:\n{rock}\n computer choice is:\n{rock}\nDRAW")
  elif comp_choice == 1:
    print(f"your choice is:\n{rock}\n computer choice is:\n{paper}\nYOU LOSE")
  elif comp_choice == 2:
    print(f"your choice is:\n{rock}\n computer choice is:\n{scissors}\nYOU WIN")
elif choice == 1:
  if comp_choice == 0:
    print(f"your choice is:\n{paper}\n computer choice is:\n{rock}\nYOU WIN")
  elif comp_choice == 1:
    print(f"your choice is:\n{paper}\n computer choice is:\n{paper}\nDRAW")
  elif comp_choice == 2:
    print(f"your choice is:\n{paper}\n computer choice is:\n{scissors}\nYOU LOSE")
elif choice == 2: 
  if comp_choice == 0:
    print(f"your choice is:\n{scissors}\n computer choice is:\n{rock}\nYOU LOSE")
  elif comp_choice == 1:
    print(f"your choice is:\n{scissors}\n computer choice is:\n{paper}\nYOU WIN")
  elif comp_choice == 2:
    print(f"your choice is:\n{scissors}\n computer choice is:\n{scissors}\nDRAW")