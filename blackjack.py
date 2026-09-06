"""
Skill: Card game logic, conditionals, value mapping
"""

def value_of_card(card):
    """Return the numerical value of a card (Ace = 1)."""
    if card in {'J', 'Q', 'K'}:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Return the higher card, or both if equal."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Return 1 or 11 for ace based on current hand."""
    if card_one == 'A' or card_two == 'A':
        return 1
    
    hand_total = value_of_card(card_one) + value_of_card(card_two)
    return 11 if hand_total <= 10 else 1

def is_blackjack(card_one, card_two):
    """Return True if hand is a blackjack (Ace + 10-value card)."""
    return (card_one == 'A' and card_two in {'10', 'J', 'Q', 'K'}) or \
           (card_two == 'A' and card_one in {'10', 'J', 'Q', 'K'})

def can_split_pairs(card_one, card_two):
    """Return True if cards have the same value."""
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Return True if hand total is between 9 and 11."""
    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
