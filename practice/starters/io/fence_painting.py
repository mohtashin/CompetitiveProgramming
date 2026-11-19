"""USACO 2015 December Bronze: Fence Painting.

Judge I/O: reads paint.in and writes paint.out.
You only need to complete solve().
"""


def solve(a, b, c, d):
    """Return the total length painted (an integer).

    Farmer John paints the interval [a, b].
    Bessie paints the interval [c, d].
    Intervals may overlap, so shared fence should not count twice.
    """
    # TODO: Write your interval solution here.
    # Return an integer, e.g. `return total_length`.
    raise NotImplementedError("Complete solve() for Fence Painting")


def main():
    # Older USACO: exact input filename matters.
    with open("paint.in", "r") as fin:
        a, b = map(int, fin.readline().split())
        c, d = map(int, fin.readline().split())

    answer = solve(a, b, c, d)

    # Older USACO: exact output filename matters.
    with open("paint.out", "w") as fout:
        fout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
