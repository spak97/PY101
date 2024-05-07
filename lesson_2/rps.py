import random

VALID_CHOICES = ['r', 'p', 's', 'l', 'S']

WINNING_COMBOS = {
    'r':     ['s', 'l'],
    'p':    ['r',     'S'],
    's':    ['p',    'l'],
    'l':   ['p',    'S'],
    'S':    ['r',     's'],
}

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def best_of_five():
    player_count = 0
    computer_count = 0

    if player_wins()
    return

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if player_wins(player, computer):
        prompt("You win!")
    elif player_wins(computer, player):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

play_again = True
win_count = 0

while play_again:
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("invalid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt("Pick again, it's best of five!")


    prompt("Do you want to play again? (y/n)")
    answer = input().lower()
    while answer not in ['y', 'n']:    
        prompt("Please enter y or n")
        answer = input().lower()

    play_again = answer == 'y'