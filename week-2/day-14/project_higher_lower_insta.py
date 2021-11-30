from art import logo, vs
import game_data
import random

def select_profile(profile_data):
  profile = profile_data[random.randint(0, len(profile_data)-1)]
  return(profile)

#select_profile(game_data.data)

def print_screen(profile_a, profile_b, logo_ascii, vs_ascii):
  print(f"{logo_ascii}\n")
  print(f"compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}\n")
  print(f"{vs_ascii}\n")
  print(f"against B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}\n")
  input("type A or B: ")


def game_logic(data):
  profile_a = select_profile(data)
  profile_b = select_profile(data)
  if profile_a == profile_b:
    profile_b = select_profile(data)
  else:
    print_screen(profile_a, profile_b, logo, vs)
    

game_logic(game_data.data)