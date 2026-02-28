import json

def merge_patch(source, patch):
    for key, pval in patch.items():
        if pval is None:
            source.pop(key, None)
        else:
            sval = source.get(key)
            if isinstance(sval, dict) and isinstance(pval, dict):
                merge_patch(sval, pval)
            else:
                source[key] = pval
    return source

source = json.loads(input().strip())
patch = json.loads(input().strip())

result = merge_patch(source, patch)
print(json.dumps(result, separators=(",", ":"), sort_keys=True))