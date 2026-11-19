"""USACO 2016 December Bronze: Square Pasture.

Judge I/O: reads square.in and writes square.out.
You only need to complete solve().
"""


def main():
    with open("square.in", "r") as fin:
        x1, y1, x2, y2 = map(int, fin.readline().split())
        x3, y3, x4, y4 = map(int, fin.readline().split())

        max_x = max(x1, x2, x3, x4)
        min_x = min(x1, x2, x3, x4)
        max_y = max(y1, y2, y3, y4)
        min_y = min(y1, y2, y3, y4)
        side1 = max_x - min_x
        side2 = max_y - min_y
        side = max(side1, side2)
        area = side * side

    with open("square.out", "w") as fout:
        fout.write(str(area) + "\n")


if __name__ == "__main__":
    main()
