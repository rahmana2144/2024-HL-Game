# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite code
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number' )
    elif low is None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            return response

        except ValueError:
            print(error)


# Guessing Loop

# replace number below with random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guesses_allowed = 5

# Set guesses used to zero at the start of each round
guesses_used = 0

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # ask the user to guess the number...
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # check that they don't want to quit
    if guess == "xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

    # check that guess is not a duplicte
    if guess in already_guessed:
        print(f"You've already ")
