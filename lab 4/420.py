g = 0

def outer(commands):
    n = 0
    def inner():
        nonlocal n
        global g
        local_var = 0
        for scope, val in commands:
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            elif scope == "local":
                local_var += val
    inner()
    return n

m = int(input().strip())
commands = []
for _ in range(m):
    scope, val = input().split()
    commands.append((scope, int(val)))

n = outer(commands)
print(g, n)