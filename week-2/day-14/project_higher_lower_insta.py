from art import logo, vs, banner
import game_data
import random

#select a random insta profile from game_data.py file data dictionary
def select_profile(profile_data):
  profile = profile_data[random.randint(0, len(profile_data)-1)]
  return(profile)

#print the selected insta profiles to console and ask user for a selection
def print_screen(profile_a, profile_b, logo_ascii, vs_ascii, banner_ascii):
  print(f"{logo_ascii}")
  print(f"{banner_ascii}")
  print(f"compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}\n")
  print(f"{vs_ascii}\n")
  print(f"against B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}\n")
  user_selection = input("type A or B: ").lower()
  if user_selection == "a":
    return("a")
  elif user_selection == "b":
    return("b")
  else:
    print("please select either A, or B")
    user_selection = input("type A or B: ").lower()


def game_logic(data):
  score = 0
  is_loser = False
  profile_a = select_profile(data)
  profile_b = select_profile(data)
  if profile_a == profile_b:
    profile_b = select_profile(data)
  else:
    while is_loser == False:
      user_selection = print_screen(profile_a, profile_b, logo, vs, banner)
      if user_selection == "a":
        if profile_a["follower_count"] > profile_b["follower_count"]:
          score+=1
          print(f"correct! your score is {score}")
          #select a new random profile for next round of play
          profile_a = select_profile(data)
          profile_b = select_profile(data)
          if profile_a == profile_b:
            profile_b = select_profile(data) 
        else:
          print(f"incorrect answer. final score: {score}")
          is_loser = True
      else:
        if profile_b["follower_count"] > profile_a["follower_count"]:
          score+=1
          print(f"correct! your score is {score}")
          #select a new random profile for next round of play
          profile_a = select_profile(data) 
          profile_b = select_profile(data)
          if profile_a == profile_b:
            profile_b = select_profile(data)
        else:
          print(f"incorrect answer. final score: {score}")
          is_loser = True

        
    
    

game_logic(game_data.data)