import random

MY_HAND_INDEX = 0
UPCARD_INDEX = 1
STICK = False
HIT = True


def basic(state) -> bool:
    """acts based on the blackjack 'basic strategy' (~45% win)."""
    hand = state[MY_HAND_INDEX]
    upcard = state[UPCARD_INDEX]
    if hand >= 17:
        return STICK
    elif 13 <= hand <= 16 and upcard < 7:
        return STICK
    elif hand == 12 and 4 <= upcard <= 6:
        return STICK
    return HIT


def rand(state) -> bool:
    """randomly choose between STICK/HIT (~29% win)"""
    return random.choice([HIT, STICK])
