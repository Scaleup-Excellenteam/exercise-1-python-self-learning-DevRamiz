from inspect import signature

def cup_of_join(*lists, sep='-'):
    import inspect
    called_with_sep = 'sep' in inspect.getcallargs(cup_of_join, *lists, sep=sep)
    result = []
    for i, lst in enumerate(lists):
        if i > 0 and called_with_sep:
            result.append(sep)
        result.extend(lst)
    if len(lists) == 1 and called_with_sep:
        result.append(sep)
    return result
