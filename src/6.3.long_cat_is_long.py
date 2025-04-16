from collections import Counter
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return dict(Counter(words))
