import json
import re

token_re = re.compile(r'(?:\.?([A-Za-z_][A-Za-z0-9_]*))|(?:\[(\d+)\])')

def resolve(root, query):
    pos = 0
    cur = root
    for m in token_re.finditer(query):
        if m.start() != pos:
            return None, False
        pos = m.end()

        key = m.group(1)
        idx = m.group(2)

        if key is not None:
            if not isinstance(cur, dict) or key not in cur:
                return None, False
            cur = cur[key]
        else:
            i = int(idx)
            if not isinstance(cur, list) or i < 0 or i >= len(cur):
                return None, False
            cur = cur[i]

    if pos != len(query):
        return None, False
    return cur, True

data = json.loads(input().strip())
q = int(input().strip())

for _ in range(q):
    query = input().strip()
    val, ok = resolve(data, query)
    if not ok:
        print("NOT_FOUND")
    else:
        print(json.dumps(val, separators=(",", ":"), sort_keys=True))