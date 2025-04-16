def cup_of_join(*lists, sep='-'):
    result = []
    explicit_sep = 'sep' in locals() or 'sep' in globals()
    if not lists:
        return result
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
