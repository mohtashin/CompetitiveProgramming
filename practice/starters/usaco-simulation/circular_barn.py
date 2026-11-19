import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")


def solve():
    # STEP 1: Read the number of rooms
    n = int(input())

    # STEP 2: Read how many cows need to reach each room
    rooms = []
    for _ in range(n):
        cows = int(input())
        rooms.append(cows)

    # STEP 3: TODO - Try each room as the entrance
    # TODO - Calculate the total walking distance for that entrance
    # TODO - Keep the smallest total distance
    answer = 0

    # STEP 4: Output the minimum total walking distance
    print(answer)


if __name__ == "__main__":
    solve()
