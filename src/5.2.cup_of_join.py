def cup_of_join(*lists, sep='-'):
    result = []
    if not lists:
        return result
    for i, lst in enumerate(lists):
        result.extend(lst)
        result.append(sep)
    return result
