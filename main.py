from art import logo, vs
from game_data import data
import random

current_compare = []

# Higher Lower game
# From data randomly pick a dictionary
# Present that information 
# Randomly pick a second dictionary
# Present that information but hide follower count
# Ask for input on if the new info follower count is higher or lower
# Compare the follower count and return wether the guess was correct or not
# If correct, remove first dictionary and generate new dictionary to continue game loop
# If not correct, display you lose and exit game

def pick_data():
    current_compare.append(data[random.randint(1, len(data))])

pick_data()
pick_data()

print(current_compare)