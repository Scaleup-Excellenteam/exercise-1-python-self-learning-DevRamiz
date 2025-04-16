def cup_of_join(*lists, sep='-'):
    result = []
    for index, l in enumerate(lists):
        if index > 0:
            result.append(sep)
        result.extend(l)
    if len(lists) == 1:
        result.append(sep)
    return result
