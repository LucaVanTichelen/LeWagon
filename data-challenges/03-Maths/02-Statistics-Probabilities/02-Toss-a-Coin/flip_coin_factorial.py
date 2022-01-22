# pylint: disable=missing-docstring

import math


def count_possibilities(n_toss, n_heads):
    '''TO DO: '''
    return math.factorial(n_toss) / (math.factorial(n_heads) *
                                     math.factorial(n_toss - n_heads))


def count_total_possibilities(n_toss):
    '''TO DO: '''
    return 2 ** n_toss


def probability(n_toss):
    '''TO DO: '''
    toss_dict = {i: 0 for i in range(n_toss + 1)}
    for i in toss_dict:
        toss_dict[i] = count_possibilities(n_toss, i) / count_total_possibilities(n_toss)
    return toss_dict
