from collections import Counter
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text.lower())
    return dict(Counter(words))
