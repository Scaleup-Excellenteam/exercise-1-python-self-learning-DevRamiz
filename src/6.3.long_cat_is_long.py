from collections import Counter
import re

def long_cat_is_long(text: str) -> dict:
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count
