import sys
from pathlib import Path
from typing import List

# Sample Input
# N and M
# 3 3
# 40 75
# 50 35
# 10 45
# 40 76
# 20 30
# 40 40


def solve(data: str) -> str:
    lines = [list(map(int, line.split())) for line in data.splitlines()]
    infraction = 0
    diff = 0
    Law = [0] * 100
    Bessie = [0] * 100
    N, M = lines[0][0], lines[0][1]
    idx = 0
    for i in range(1, N + 1):
        amount = lines[i][0]
        limit = lines[i][1]
        for j in range(amount):
            Law[idx] = limit
            idx += 1
    idx = 0
    for i in range(N + 1, len(lines)):
        amount = lines[i][0]
        limit = lines[i][1]
        for j in range(amount):
            Bessie[idx] = limit
            idx += 1
    for i in range(100):
        diff = Bessie[i] - Law[i]
        if diff > infraction:
            infraction = diff
    return str(infraction) + "\n"


def main() -> None:
    prob = "speeding"  # set to "problem_name" for USACO file I/O

    if prob is not None and Path(f"{prob}.in").exists():
        data = Path(f"{prob}.in").read_text()
        result = solve(data)
        Path(f"{prob}.out").write_text(result)
    else:
        data = sys.stdin.read()
        sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()

# Input patterns you may use in solve():

# 1. Default pattern: all tokens as integers
# nums = list(map(int, data.split()))

# 2. Read lines, each line is a list of integers
# lines = [list(map(int, line.split())) for line in data.splitlines()]

# 3. Read a single integer, then a list of integers
# it = iter(data.split())
# n = int(next(it))
# arr = [int(next(it)) for _ in range(n)]

# 4. Read a single integer (or other type) from the start
# it = iter(data.split())
# x = int(next(it))

# 5. Read multiple values of different types
# it = iter(data.split())
# a = int(next(it))
# b = float(next(it))
# s = next(it)
