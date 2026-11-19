import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")


def solve():
    # STEP 1: Read the number of road and driving segments
    n, m = map(int, input().split())

    # STEP 2: Read each road segment (length, speed limit)
    road = []
    for _ in range(n):
        length, limit = map(int, input().split())
        road.append((length, limit))

    # STEP 3: Read each driving segment (length, Bessie's speed)
    bessie = []
    for _ in range(m):
        length, speed = map(int, input().split())
        bessie.append((length, speed))

    # STEP 4: TODO - Simulate the 100 miles and find the largest speeding amount
    answer = 0

    # STEP 5: Output the largest speeding amount
    print(answer)


if __name__ == "__main__":
    solve()
