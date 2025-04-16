from typing import Generator

def generator_interleave(a: list, b: list) -> Generator:
    for x, y in zip(a, b):
        yield x
        yield y
