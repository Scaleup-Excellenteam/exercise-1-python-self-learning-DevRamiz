def cup_of_join(*lists, sep='-'):
    result = []
    for i, lst in enumerate(lists):
        if i > 0:
            result.append(sep)
        if lst:
            result.extend(lst)
        else:
            result.append(sep)
    if len(lists) == 1:
        result.append(sep)
    return result
