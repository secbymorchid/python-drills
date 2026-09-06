"""
Skill: Arithmetic operations, division, modulo, floor division
"""

def exchange_money(budget, exchange_rate):
    """Return exchanged currency value."""
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """Return remaining budget after exchange."""
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """Return total value of bills."""
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """Return number of whole bills."""
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    """Return leftover amount after bills."""
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Return maximum exchangeable value with spread and denomination."""
    actual_rate = exchange_rate * (1 + spread / 100)
    max_currency = budget / actual_rate
    return int(max_currency // denomination * denomination)
