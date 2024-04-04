import math
import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # check use response, question
        # repeats if users say yes / no

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

**** Instructions ****

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the 
secret number will be between 1 and 100).

Then choose how many rounds you'd like to play <enter> for 
infinite mode.

Your goal is to try to guess the secret number without
running out of guess.

Good luck.


    ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game

def int_check(question, low=None, high=None, exit_code=None):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == exit_code:
            return "infinite"
        try:
            response = int(to_check)

            # checks that the number is valid
            if response < low:
                print(error)
            elif response > high:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("🔼🔼🔼 Welcome to Higher Lower Game 🔻🔻🔻")
print()

want_instructions = yes_no("Do you want to read the instructions?")

# checks user for number of rounds / infinite mode
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

#  allow user to choose the high / lower number
else:
    low_num = int_check("Low Number?")
    high_num = int_check("High number? ", low=low_num + 1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round  {rounds_played + 1} (Infinite mode) "
    else:

        rounds_heading = f"\n💿💿💿 Rounds {rounds_played + 1} of {num_rounds}💿💿💿"

    print(rounds_heading)

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)
    print("Spoiler Alert", secret)  # remove this line after testing

    guess = ""
    while guess != secret and guesses_used < guesses_allowed
    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here


# Game history / Statistics area
