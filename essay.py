"""
Skill: String methods, booleans, whitespace handling
"""

def capitalize_title(title):
    """Return title with first letter of each word capitalized."""
    return title.title()

def check_sentence_ending(sentence):
    """Return True if sentence ends with a period."""
    return sentence.endswith('.')

def clean_up_spacing(sentence):
    """Return sentence with leading/trailing whitespace removed."""
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    """Return sentence with all occurrences of old_word replaced by new_word."""
    return sentence.replace(old_word, new_word)
