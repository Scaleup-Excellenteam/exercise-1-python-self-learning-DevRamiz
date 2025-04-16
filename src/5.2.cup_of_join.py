def cup_of_join(*lists, sep=None):
    from inspect import currentframe, getargvalues
    frame = currentframe()
    args, _, _, values = getargvalues(frame.f_back)
    explicit_sep = 'sep' in values

    result = []
    for i, lst in enumerate(lists):
        if i > 0 and explicit_sep:
            result.append(sep)
        if lst:
            result.extend(lst)
        else:
            if explicit_sep:
                result.append(sep)
    if len(lists) == 1 and explicit_sep:
        result.append(sep)
    return result
