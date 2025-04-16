def interleave(a: list, b: list) -> list:
    return [val for pair in zip(a, b) for val in pair]
