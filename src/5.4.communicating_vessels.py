from typing import Generator
from itertools import zip_longest

def generator_interleave(*args) -> Generator:
    for group in zip_longest(*args, fillvalue=None):
        for item in group:
            if item is not None:
                yield item

def interleave(*args):
    return list(generator_interleave(*args))
