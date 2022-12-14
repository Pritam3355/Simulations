import numpy as np
import random
import copy

org_deck = [
'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
]
# S = spade,D = diamond,C = club,H = heart,J = joker,K = king, Q= queen

# What is the probability that at least 2 Kings will appear next to each other in 
# the shuffled deck? 

# so we can have 'KK' , 'KKK' , 'KK + anything + KK',...
# p(2 kings appear next to each other) = 1 - p(no 2 king appear next to each other)
# if we remove 4 kings we have 48 cards with 49 places to place 4 kings 
# so they won't appear together = 49P4 = 49!/(49-4)!
# remaining cards can be arranged in 48! ways
# so p(no 2 king appear next to each other) = (49P4 * 48!)/52! 
# 1 - p(no 2 king appear next to each other) = 0.21


def helper(deck):
    for i in range(len(deck)-1):
        if deck[i][0] == 'K' and deck[i+1][0] == 'K':
            return True

def solve(n):
    res = 0
    for _ in range(n):
        deck = copy.deepcopy(org_deck)
        random.shuffle(deck)
        if helper(deck): res += 1
    print(res*100/n)

for i in range(1, 7):
    solve(10**i)


# 40.0
# 20.0
# 22.7
# 21.84
# 22.016
# 21.73



# What is the probability that at least one King and one Queen will be next 
# to each other or one card away? 

def helper(deck):
    n = len(deck)
    for i in range(n-1):
        if deck[i][0] + deck[i+1][0] in ['KQ', 'QK']:
            return True
        if i!=n-2:
            if deck[i][0] + deck[i+2][0] in ['KQ', 'QK']:
                return True

def solve(n):
    res = 0
    for _ in range(n):
        deck = copy.deepcopy(org_deck)
        random.shuffle(deck)
        if helper(deck): res += 1
    print(res*100/n)

for i in range(1, 7):
    helper(10**i)


# 80.0
# 71.0
# 71.0
# 73.64
# 73.648
# 73.6362
