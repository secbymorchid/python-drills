"""
Skill: Boolean logic, conditionals, efficiency calculations
"""

def is_criticality_balanced(temperature, neutrons_emitted):
    """Return True if reactor is in criticality balance."""
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Return efficiency band of the reactor."""
    efficiency = (voltage * current) / theoretical_max_power * 100
    
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Return reactor status based on criticality threshold."""
    criticality = temperature * neutrons_produced_per_second
    
    if criticality < 0.9 * threshold:
        return 'LOW'
    elif criticality <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
