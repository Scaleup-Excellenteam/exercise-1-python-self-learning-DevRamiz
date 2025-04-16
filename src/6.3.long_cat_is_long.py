import re
from collections import Counter

def long_cat_is_long(text):
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return Counter(words)
