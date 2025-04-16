from collections import defaultdict
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'[a-zA-Z]{2,}', text.lower())
    d = defaultdict(int)
    for word in words:
        d[word] += len(word)
    return dict(d)
