"""
Skill: List operations, slicing, averages, list concatenation
"""

def get_rounds(number):
    """Return list of three rounds starting with number."""
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    """Return combined list of rounds."""
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Return True if number is in rounds list."""
    return number in rounds

def card_average(hand):
    """Return average of card values in hand."""
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    """Return True if first/last average or median equals actual average."""
    avg = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    median = hand[len(hand) // 2]
    return avg == first_last_avg or avg == median

def average_even_is_average_odd(hand):
    """Return True if average of even-indexed cards equals odd-indexed."""
    return card_average(hand[::2]) == card_average(hand[1::2])

def maybe_double_last(hand):
    """Return hand with last card doubled if it's a Jack (11)."""
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
