import random

target_number = random.randint(1, 100)

print("welcome to number guessing game")
print("i'm thinking of a number between 1 and 100")
difficulty = input("choose difficulty - type 'easy' or 'hard'").lower()

if difficulty == "easy":
  guesses = 10
else:
  guesses = 5

while guesses > 0:
  guess = int(input("guess a number: "))
  if guess > target_number:
    print("too high, guess again")
    guesses -= 1
    print(f"you have {guesses} guesses remaining")
  elif guess < target_number: 
    print("too low, guess again")
    guesses -= 1
    print(f"you have {guesses} guesses remaining")
  else:
    print("correct, you win!")
    break