#rock, paper, scissors

import random


def play():
    user = input("Whats your choice?: 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'win'

    return 'lose'


def is_win(player, opponent):
    # returns true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 's' and opponent ==
                                                                                      'p'):
        return True


print(play())

