import math

# k = int(input())
k = 8
total = k * k

moves = 6 * total - (
    4 * 3 + 8 * 4 + (k - 4) * 4 * 5 + 4 * 5 + 8 * 7 + ((k - 4) ** 2) * 9
)
print(moves**2)
