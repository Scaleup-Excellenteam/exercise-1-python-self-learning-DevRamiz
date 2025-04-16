def cup_of_join(*lists, sep='-'):
    result = []
    for i, l in enumerate(lists):
        result.extend(l)
        if i != len(lists) - 1 or len(lists) == 1:
            result.append(sep)
    return result
