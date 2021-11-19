import os
from auction_art import logo

def clear():
  os.system("clear")

bids = {}
more_bids = True

#print(logo)
print("welcome to secret auction")

while more_bids == True:
  name = input("what is your name?: ")
  bid = int(input("what is your bid?: $"))
  bids[name] = bid
  next_bid = input("more people to place bids? (y or n): ")
  if next_bid == "n":
    more_bids = False

def calc_bids(bid_list):
  highest_bid_name = ""
  highest_bid_amount = 0
  for name in bid_list:
    #print(bid_list[name])
    if bid_list[name] > highest_bid_amount:
      highest_bid_name = name
      highest_bid_amount = bid_list[name]
  print(f"the highest bidder was {highest_bid_name} with a bid of: ${highest_bid_amount}")

calc_bids(bids)    
#print(bids)
