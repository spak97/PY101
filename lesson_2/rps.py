import random

VALID_CHOICES = ['r', 'p', 's', 'l', 'S']

WINNING_COMBOS = {
    'r':     ['s', 'l'],
    'p':    ['r',     'S'],
    's':    ['p',    'l'],
    'l':   ['p',    'S'],
    'S':    ['r',     's'],
}


player_count = 0
computer_count = 0
winner = ""

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]


def best_of_five():
    global player_count, computer_count, winner
    winner = display_winner(choice, computer_choice)

    if "Player" in winner:
        player_count += 1
    elif "Computer" in winner:
        computer_count += 1

def determine_winner():
    if player_count == 3:
        winner = "Player"
        return winner
    elif computer_count == 3:
        winner = "Computer"
        return winner


def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if player_wins(player, computer):
        prompt("You win this round!")
        return "Player"
    elif player_wins(computer, player):
        prompt("Computer wins this round!")
        return "Pomputer"
    else:
        prompt("It's a tie this round!")
        return "tie"

play_again = True

while play_again:
    prompt(f"Choose one: {", ".join(VALID_CHOICES)}")
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("invalid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    best_of_five()

    print(determine_winner())

    print(winner)
    print(player_count)
    print(computer_count)

    # if final winner has been decided
    if determine_winner() == "Player" or determine_winner() == "Computer":
        prompt(f"{winner} is the final winner!")
        prompt("Do you want to play again? (y/n)")
        answer = input().lower()
        while answer not in ['y', 'n']:    
            prompt("Please enter y or n")
            answer = input().lower()

        play_again = answer == 'y'
        player_count = 0
        computer_count = 0
    
    prompt("Pick again, it's best of five!")