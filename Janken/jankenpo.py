'''
This program is a simulation of the classic game, Rock Paper Scissors.
I called this program, Jankenpo, which is the Japanese phrase for the game.
This program uses two functions to check the user input and decide the winner.
All calls are made from the main function.
'''

# This function takes the user's choice and checks to make sure that it is within the right parameter for the game.
def roll(throw):
    throw = int(input("What will you throw out!?"))
    while throw < 1 or throw > 3:
            throw = int(input("Please re-enter your choice with the correct number. 1 = Rock, 2 = Paper, 3 = Scissors"))

    return(throw)

# This function takes the two checked choices of the players and determines the winner of the game.
def winner(playerone, playertwo):
    if playerone == 1 and playertwo == 2:
        print("Paper beats Rock! Player Two wins!")
    elif playerone == 1 and playertwo == 3:
        print("Rock beats Scissors! Player One wins!")
    elif playerone == 2 and playertwo == 1:
        print("Paper beats Rock! Player One wins!")
    elif playerone == 2 and playertwo == 3:
        print("Scissors beats Paper! Player Two wins!")
    elif playerone == 3 and playertwo == 2:
        print("Scissors beats Paper! Player One wins!")
    elif playerone == 3 and playertwo == 1:
        print("Rock beats Scissors! Player Two wins!")

if __name__ == '__main__':
    player_one = 0
    player_two = 0
    choice = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Your choices are 1 for Rock, 2 for Paper and 3 for Scissors")

    print("Player One first!")
    player_one = roll(choice)
    print("Player Two next!")
    player_two = roll(choice)

    # If the choices are the same, there is no need to call the function to determine the winner.
    if player_one == player_two:
        print("Its a draw game, let's try that again")
    else:
        winner(player_one, player_two)

