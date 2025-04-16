from collections import defaultdict

def group_by(items: list[str]) -> dict[str, list[str]]:
    grouped = defaultdict(list)
    for item in items:
        grouped[item[0]].append(item)
    return dict(grouped)

group_by = group_by
