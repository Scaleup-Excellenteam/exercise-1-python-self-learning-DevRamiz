def interleave(a, b):
    for x, y in zip(a, b):
        yield x
        yield y
