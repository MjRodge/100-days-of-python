import art
import game_data
import random

def select_profile(profile_data):
  profile = profile_data[random.randint(0, len(profile_data)-1)]
  print(profile)

select_profile(game_data.data)