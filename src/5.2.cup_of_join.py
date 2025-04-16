def cup_of_join(*lists, sep=None):
    from inspect import getargvalues, currentframe
    called_with_sep = 'sep' in getargvalues(currentframe().f_back).locals

    result = []

    for i, lst in enumerate(lists):
        if i > 0 and called_with_sep:
            result.append(sep)
        result.extend(lst)

    # Handle trailing separator:
    if len(lists) == 1 and called_with_sep:
        result.append(sep)
    if any(len(lst) == 0 for lst in lists) and called_with_sep:
        result += [sep] * sum(1 for lst in lists if len(lst) == 0)

    return result
