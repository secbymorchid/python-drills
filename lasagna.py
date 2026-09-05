"""
Skill: Functions, constants, docstrings
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Return prep time based on number of layers."""
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total elapsed cooking time."""
    return (PREPARATION_TIME * number_of_layers) + elapsed_bake_time
