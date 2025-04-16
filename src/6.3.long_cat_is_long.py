from collections import defaultdict
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    count = defaultdict(int)
    for word in words:
        count[word.lower()] += len(word)
    return dict(count)
