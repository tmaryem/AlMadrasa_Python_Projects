import random

def is_winner(player, pc):

    #define the winning combinations 
    winning_combinations = {
          'r' : 's', # Rock beats Scissors
          's' : 'p', # Scissors beats Paper
          'p' : 'r' # Paper beats Rock
     }
    return winning_combinations[player] == pc

def play_game():
    # Start the game
    print("The game is starting between you and the PC.")

    # List of valid choices
    choices = ['r', 'p', 's']

    # Ask the player to choose one option 
    user = input("Please enter your choice: r for Rock, p for paprer, or s for Scissors:\n").lower()
    pc = random.choice(choices)

    # Validate the user's input
    while user not in choices:
            print("Invalid choice! Please enter 'r', 'p', or 's'.")
            user = input("Enter your choice: ").lower()

    print("Your choice : ", user)
    print("Pc choice : ", pc)

    # Determine the result based on the choices
    if(user==pc):
        print("it's a tie!!")
    elif is_winner(user, pc):
        print("You win!!")
    else:
        print("PC win!!")

def main():
     while True:
          # Start a new game
          play_game()
          replay = input("\nDo you want to play again?\n(y/n):").lower()
          if replay != 'y':
               print("Thank you for playing our game, goodbye!!")
               break
          
if __name__ == "__main__":
     main()
