# pylint: disable=missing-docstring

from flip_coin_factorial import probability
from simulate_reality import play_n_game


def mean_squared_error(n_games, n_toss):
    '''TO DO: return the squared error between the theoretical and "actual"
     results (obtained through simulation)'''
    prob = probability(n_toss)
    real = play_n_game(n_games, n_toss)
    total = 0
    for i in prob:
        total += (prob[i] - real[i])**2
    total /= n_toss
    return total
