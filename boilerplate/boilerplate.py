import sys
from pathlib import Path
from typing import List

def solve(data: str) -> str:
    # Default: map all tokens as integers
    nums = list(map(int, data.split()))

    # Example solution using nums:
    result = sum(nums)  # Example logic
    return str(result) + "\n"

def main() -> None:
    prob = None  # set to "problem_name" for USACO file I/O

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
