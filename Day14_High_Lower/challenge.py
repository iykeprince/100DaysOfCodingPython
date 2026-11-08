# Display art
from game_art import logo, vs
from game_data import data
import random


def format_data(account):
    """Format account data into printable format."""
    # Format the account data into printable format
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower count and return if they got it right."""
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)

game_should_continue = True
score = 0
account_b = random.choice(data)

while game_should_continue:
    # Generate random account from the list of game data dictionaries
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear this screen
    print("\n"*20)

    # Check if user is correct
    ## Get follower count of each account 
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    ## Use if statement to check if user's correct
    if is_correct:
        score += 1
        print(f"You're right: Your score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False

# Give user feedback on their guess.

# Make the game repeatable 

## Make the account at position B become the next account at position A 