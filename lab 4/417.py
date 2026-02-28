import math

r = float(input().strip())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

dx, dy = bx - ax, by - ay
a = dx*dx + dy*dy

if a == 0.0:
    inside = (ax*ax + ay*ay) <= r*r + 1e-12
    print(f"{0.0:.10f}")
    raise SystemExit

b = 2.0 * (ax*dx + ay*dy)
c = ax*ax + ay*ay - r*r
disc = b*b - 4*a*c

if disc < 0:
    inside = (ax*ax + ay*ay) <= r*r + 1e-12
    ans = math.sqrt(a) if inside else 0.0
else:
    s = math.sqrt(max(0.0, disc))
    t1 = (-b - s) / (2*a)
    t2 = (-b + s) / (2*a)
    if t1 > t2: t1, t2 = t2, t1
    L = max(0.0, t1)
    R = min(1.0, t2)
    ans = (R - L) * math.sqrt(a) if R > L else 0.0

print(f"{ans:.10f}")