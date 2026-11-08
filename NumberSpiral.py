import sys

t = int(sys.stdin.readline())

ans = 0

for _ in range(t):
    y, x = map(int, sys.stdin.readline().split())

    if x > y:
        d = x**2 + (1 - x)
        if x % 2 == 0:  # even and x goes down
            ans = d - (x - y)
        else:
            ans = d + (x - y)
    elif y > x:
        d = y**2 + (1 - y)
        if y % 2 == 0:  # even and y goes up
            ans = d + (y - x)
        else:
            ans = d - (y - x)
    else:
        d = y**2 + (1 - y)
        ans = d
    print(ans)
