def cup_of_join(*lists, sep='-'):
    result = []
    for l in lists:
        result.extend(l)
        result.append(sep)
    if result:
        result.pop()  # remove last sep
    return result
