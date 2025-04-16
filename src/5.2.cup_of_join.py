from inspect import signature

def cup_of_join(*lists, sep='-'):
    sig = signature(cup_of_join)
    sep_was_explicit = 'sep' in sig.bind_partial(*lists).arguments
    result = []
    for i, l in enumerate(lists):
        if i > 0 and sep_was_explicit:
            result.append(sep)
        result.extend(l)
    if len(lists) == 1 and sep_was_explicit:
        result.append(sep)
    return result
