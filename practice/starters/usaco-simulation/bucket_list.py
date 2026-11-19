import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")


def solve():
    # STEP 1: Read the number of cows
    n = int(input())  # 3

    # STEP 2: Read each cow's start time, end time, and buckets needed
    cows = []
    maxvar = 0
    for _ in range(n):
        start, end, buckets = map(int, input().split())
        cows.append((start, end, buckets))
        if end >= maxvar:
            maxvar = end

    # STEP 3: TODO - Simulate the buckets being used over time
    answer = 0
    current = 0
    for i in range(1, maxvar):

        for j in range(len(cows)):
            if cows[j][0] == i:
                current += cows[j][2]
            if cows[j][1] == i:
                current -= cows[j][2]
        if current >= answer:
            answer = current

    # STEP 4: Output the minimum number of buckets needed
    print(answer)


if __name__ == "__main__":
    solve()
