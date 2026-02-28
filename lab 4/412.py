import json

MISSING = object()

def to_json(v):
    if v is MISSING:
        return "<missing>"
    return json.dumps(v, separators=(",", ":"), sort_keys=True)

def deep_diff(a, b, prefix=""):
    diffs = []
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            pa = a.get(k, MISSING)
            pb = b.get(k, MISSING)
            path = f"{prefix}.{k}" if prefix else k
            if isinstance(pa, dict) and isinstance(pb, dict):
                diffs.extend(deep_diff(pa, pb, path))
            else:
                if pa is MISSING or pb is MISSING or pa != pb:
                    diffs.append((path, f"{path} : {to_json(pa)} -> {to_json(pb)}"))
    else:
        if a != b:
            diffs.append((prefix, f"{prefix} : {to_json(a)} -> {to_json(b)}"))
    return diffs

obj1 = json.loads(input().strip())
obj2 = json.loads(input().strip())

diffs = deep_diff(obj1, obj2)
if not diffs:
    print("No differences")
else:
    for _, line in sorted(diffs, key=lambda x: x[0]):
        print(line)