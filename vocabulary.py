"""
Skill: Prefixes, suffixes, string manipulation, list comprehensions
"""

def add_prefix_un(word):
    """Return word with 'un' prefix added."""
    return "un" + word

def make_word_groups(vocab_words):
    """Apply prefix to all words and return formatted string."""
    prefix = vocab_words[0]
    words = vocab_words[1:]
    prefixed_words = [prefix + word for word in words]
    all_words = [prefix] + prefixed_words
    return ' :: '.join(all_words)

def remove_suffix_ness(word):
    """Remove 'ness' suffix, handling 'iness' → 'y' rule."""
    if word.endswith("iness"):
        return word[:-5] + "y"
    else:
        return word[:-4]

def adjective_to_verb(sentence, index):
    """Extract adjective from sentence and add 'en' suffix."""
    words = sentence.split()
    return words[index].strip('.') + "en"
