import sys


def main():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        # Room dimensions
        W, H = map(int, input().split())

        # Existing table coordinates
        x1, y1, x2, y2 = map(int, input().split())

        # New table dimensions
        w, h = map(int, input().split())

        # ==========================================
        # YOUR SOLUTION GOES HERE
        # ==========================================

        # Calculate the minimum distance needed
        # to move the existing table.

        # Store your answer in: distance
        # Use -1 if no valid arrangement exists.

        raise NotImplementedError("Write your solution here")

        # ==========================================
        # OUTPUT (Already handled)
        # ==========================================

        if distance == -1:
            print(-1)
        else:
            print(f"{distance:.9f}")


if __name__ == "__main__":
    main()
