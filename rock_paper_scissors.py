###################################################################################################
# File Name: rock_paper_scissors.py
# Description: A program that allows the user to play against a computer in rock paper scissors,
# for 5 rounds.
# Author: Matthew Elliott
# Date: 3/26/2024
###################################################################################################

import random

# A constant for the number of rounds played
ROUNDS = 5
# Constant that determines who wins
WIN = 3

# A Dictionary of valid moves the user or the computer can make
moves = {
    'ROCK': 0,
    'SCISSORS': 1,
    'PAPER': 2,
}

cpu_wins = 0

player_wins = 0

draws = 0



def main():
    name = ""
    round = 0
    while ((round < ROUNDS) and (cpu_wins < WIN) and (player_wins < WIN)):
        if round == 0:
            name = prompt_user()
            print()

        cpu = computer_chooses()
        user = user_chooses()

        result = compare_hands(cpu, user)

        print_round(user, cpu, result)

        update_score(result)

        # update rounds
        round+=1
    print_game(name)




def compare_hands(computer, player):
    # an array of comparisons between the user and the computer going by Rock Scissor, and paper.
    #                        
    #                                   Player:
    #
    #                        |  ROCK  |  Scissor  |  PAPER  |
    #               ROCK     |   0    |    -1     |    1    |
    #   Computer:   SCISSOR  |   1    |     0     |   -1    |
    #               PAPER    |  -1    |     1     |    0    |
    #
    RSP_list = [[0, -1, 1], 
                [1, 0, -1], 
                [-1, 1, 0]]
    return RSP_list[computer][player]

def prompt_user():
    return input("Enter your name >>> ")

def computer_chooses():
    return random.randint(0,2)

def user_chooses():
    to_return = 0

    valid_input = False

    while not valid_input:

        choice = input("Choose one: ROCK, PAPER, SCISSORS >>> ")
        choice = choice.upper()
        try:
            to_return = moves[choice]
            valid_input = True
        except:
            print("Invalid choice please try again\n")
    
    return to_return

def update_score(result):
    if result == 1:
        global player_wins
        player_wins += 1
    elif result == -1:
        global cpu_wins
        cpu_wins += 1
    else:
        global draws
        draws += 1

def print_round(user, cpu, result):
    # list out keys and values separately
    key_list = list(moves.keys())
    value_list = list(moves.values())

    user_choice = value_list.index(user)
    cpu_choice = value_list.index(cpu)

    print("You chose:", key_list[user_choice],"\n")
    print("Computer chose:", key_list[cpu_choice],"\n")

    if result > 0:
        print("Congrats You won the round\n")
    elif 0 > result:
        print("I won this round, better luck next time !\n")
    else:
        print("We tied this round\n")

def print_game(name):
    print(name, ": ", player_wins, "wins,", cpu_wins, "loss,", draws, "draw\n")
    print("Computer:", cpu_wins, "wins,", player_wins, "loss,", draws, "draw\n")

    if player_wins > cpu_wins:
        print("Congrats", name + ", You Win!\n")
    elif cpu_wins > player_wins:
        print( "I win, better luck next time", name + "!\n")
    else:
        print("We tie! That was fun, You are a worthy adversary. Let's play again sometime\n", name)

if __name__ == "__main__":
    main()