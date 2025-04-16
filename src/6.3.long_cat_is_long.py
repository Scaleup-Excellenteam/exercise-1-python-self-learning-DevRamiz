from collections import Counter
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text)
    d = Counter()
    for word in words:
        d[word] += 1
    return d
