from collections import defaultdict

def group_by(key_func, items):
    grouped = defaultdict(list)
    for item in items:
        grouped[key_func(item)].append(item)
    return dict(grouped)
