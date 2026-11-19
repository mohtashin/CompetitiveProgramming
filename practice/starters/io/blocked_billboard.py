"""USACO 2017 December Bronze: Blocked Billboard (NOT Blocked Billboard II).

Judge I/O: reads billboard.in and writes billboard.out.
You only need to complete solve().
"""


def solve(billboard1, billboard2, truck):
    """Return the total visible area of the two billboards (an integer).

    Each rectangle is a tuple (x1, y1, x2, y2):
        (x1, y1) is its bottom-left corner,
        (x2, y2) is its top-right corner.

    billboard1, billboard2: rectangles being advertised
    truck: rectangle that may cover the billboards
    """
    # TODO: Write your geometry/overlap solution here.
    # Return an integer, e.g. `return visible_area`.
    raise NotImplementedError("Complete solve() for Blocked Billboard")


def main():
    # Older USACO problem: file-based input, NOT input().
    with open("billboard.in", "r") as fin:
        billboard1 = tuple(map(int, fin.readline().split()))
        billboard2 = tuple(map(int, fin.readline().split()))
        truck = tuple(map(int, fin.readline().split()))

    # Only this function needs your code.
    answer = solve(billboard1, billboard2, truck)

    # Older USACO problem: file-based output, NOT print().
    with open("billboard.out", "w") as fout:
        fout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
