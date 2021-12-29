from art import logo, vs
from game_data import data
from os import system, name
import random


current_compare = []
score = 0

# Higher Lower game
# Present that information 
# Randomly pick a second dictionary
# Present that information but hide follower count
# Ask for input on if the new info follower count is higher or lower
# Compare the follower count and return wether the guess was correct or not
# If correct, remove first dictionary and generate new dictionary to continue game loop
# If not correct, display you lose and exit game

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def pick_data():
    current_compare.append(data[random.randint(1, len(data))])

def game_setup():
    pick_data()
    pick_data()
    game_loop()

def game_loop():
    global score
    clear()
    print(logo)
    print(f"Name: {current_compare[0]['name']} \nTotal Followers: {current_compare[0]['follower_count']} \nDescription: {current_compare[0]['description']} \nCountry: {current_compare[0]['country']}")
    print(vs)
    print(f"Name: {current_compare[1]['name']} \nTotal Followers: ???? \nDescription: {current_compare[1]['description']} \nCountry: {current_compare[1]['country']}\n")
    guess = input(f"Is the number of followers of {current_compare[1]['name']} higher or lower than {current_compare[0]['name']}: ").lower()
    if guess == "higher":
        if str(current_compare[0]['follower_count']) < str(current_compare[1]['follower_count']):
            print("That's correct, here is the next round.")
            current_compare.pop(0)
            score = score + 1
            pick_data()
            game_loop()
        elif str(current_compare[0]['follower_count']) > str(current_compare[1]['follower_count']):
            print(f"That's incorrect, your score was {str(score)}. \nTry again.")
    elif guess == "lower":
        if str(current_compare[0]['follower_count']) > str(current_compare[1]['follower_count']):
            print("That's correct, here is the next round.")
            current_compare.pop(0)
            score = score + 1
            pick_data()
            game_loop()
        elif str(current_compare[0]['follower_count']) < str(current_compare[1]['follower_count']):
            print(f"That's incorrect, your score was {str(score)}. \nTry again.")


game_setup()