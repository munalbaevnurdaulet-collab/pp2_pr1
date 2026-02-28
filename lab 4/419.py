import math

r = float(input().strip())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

EPS = 1e-12
TWOPI = 2.0 * math.pi

def dist(x, y):
    return math.hypot(x, y)

def seg_min_dist_to_origin(ax, ay, bx, by):
    vx, vy = bx - ax, by - ay
    a2 = vx*vx + vy*vy
    if a2 < EPS:
        return dist(ax, ay)
    t = -(ax*vx + ay*vy) / a2
    t = 0.0 if t < 0.0 else (1.0 if t > 1.0 else t)
    px, py = ax + t*vx, ay + t*vy
    return dist(px, py)

def tangent_angles(x, y):
    d = dist(x, y)
    theta = math.atan2(y, x)
    if d <= r + EPS:
        return [theta]
    alpha = math.acos(r / d)
    return [theta - alpha, theta + alpha]

def ang_diff(a, b):
    d = (b - a) % TWOPI
    return min(d, TWOPI - d)


if seg_min_dist_to_origin(ax, ay, bx, by) >= r - 1e-10:
    ans = dist(bx - ax, by - ay)
    print(f"{ans:.10f}")
    raise SystemExit

da, db = dist(ax, ay), dist(bx, by)
ta = math.sqrt(max(0.0, da*da - r*r))
tb = math.sqrt(max(0.0, db*db - r*r))

Aang = tangent_angles(ax, ay)
Bang = tangent_angles(bx, by)

best = float("inf")
for a1 in Aang:
    for b1 in Bang:
        best = min(best, ta + tb + r * ang_diff(a1, b1))

print(f"{best:.10f}")