from collections import defaultdict
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z]{2,}\b', text)
    counter = defaultdict(int)
    for word in words:
        counter[word] += 1
    return dict(counter)
