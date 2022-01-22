# pylint: disable=missing-docstring

import random


def play_one_game(n_toss):
    '''TO DO: return the number of heads'''
    heads_counter = 0
    for _ in range(n_toss):
        if random.randint(0, 1) == 1:
            heads_counter += 1
    return heads_counter


def play_n_game(n_games, n_toss):
    '''TO DO: return a dictionary.
    The keys will be the possible head counts of each game
    The values will correspond to the probability of a game ending with that
     number of heads.
    '''
    total = {toss: 0 for toss in range(n_toss + 1)}
    for _ in range(n_games):
        result = play_one_game(n_toss)
        total[result] += 1 / n_games
    return total
