from typing import Generator

def generator_interleave(*args) -> Generator:
    for group in zip(*args):
        for item in group:
            yield item

def interleave(*args):
    return list(generator_interleave(*args))
