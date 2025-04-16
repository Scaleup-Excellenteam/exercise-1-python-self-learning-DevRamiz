def cup_of_join(*lists, sep='-'):
    result = []
    for i, l in enumerate(lists):
        if i > 0 and sep is not None:
            result.append(sep)
        result.extend(l)
    if len(lists) == 1 or any(len(l) == 0 for l in lists):
        if sep is not None:
            result.append(sep)
    return result
