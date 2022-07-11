#Rock, paper, scissors game.....

import random
import time

name = input('What is your name?: ')
wins = 0
rounds = 0
ties = 0

while True:
    individual = ''

    game = ['rock', 'paper', 'scissors']

    while len(individual) == 0 or individual.casefold() not in game:
        individual = input('rock, paper or scissors?: ')

    computer = random.choice(game)

    print(name + ':', individual)
    time.sleep(1)
    print('Computer:', computer)
    time.sleep(1)

    if computer == individual.casefold():
        print('Tie!')
        ties += 1
    elif computer == 'rock' and individual.casefold() == 'paper' or computer == 'paper' and individual.casefold() == 'scissors' or computer == 'scissors' and individual.casefold() == 'rock':
        print('You Win!')
        wins += 1
    else:
        print('You Lose!')
    time.sleep(1)

    rounds += 1

    ans = input('Wanna Play Again? (Yes/No): ').casefold()
    time.sleep(1)

    computer_score = rounds - wins - ties

    if ans == 'no':
        time.sleep(1)
        print('\nNumber of rounds: ' + str(rounds))
        time.sleep(1)
        print('Computer\'s score: ' + str(computer_score))
        time.sleep(1)
        print(name + '\'s score:', str(wins))
        time.sleep(1)
        print('Tie(s): ' + str(ties))
        break

print('\n\nThanks For Playing :)')
