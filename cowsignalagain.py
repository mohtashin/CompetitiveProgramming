import sys
from pathlib import Path
from typing import List

# Sample Input
sample_input = """5 4 2
XXX.
X..X
XXX.
X..X
XXX."""


def solve(data: str) -> str:
    newdata = data.splitlines()
    M, N, K = map(int, newdata[0].split())
    print(f"{M}, {N}, {K}")
    lines = newdata[1:]
    print(lines)
    return ""
    # newData = data.split()
    # M = int(newData[0])
    # N = int(newData[1])
    # K = int(newData[2])
    # offset = 3
    # res = ""
    # for m in range(M):
    #     for k1 in range(K):
    #         for n in range(N):
    #             for k2 in range(K):
    #                 res += (newData[m + offset])[n]
    #         res += "\n"
    # return res


def main() -> None:
    prob = "cowsignal"

    if prob is not None and Path(f"{prob}.in").exists():
        data = Path(f"{prob}.in").read_text()
        result = solve(data)
        Path(f"{prob}.out").write_text(result)
    else:
        data = """5 4 2
        XXX.
        X..X
        XXX.
        X..X
        XXX."""
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
