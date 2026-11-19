"""Codeforces 1216C: White Sheet.

Judge I/O: stdin and stdout (no .in/.out files).
You only need to complete solve().
"""


def solve(white_sheet, black_sheet1, black_sheet2):
    """Return True if any of the white sheet remains visible, else False.

    Each rectangle is (x1, y1, x2, y2), with bottom-left and
    top-right corners respectively.
    """
    # TODO: Write your rectangle coverage solution here.
    # Return a Boolean, e.g. `return is_visible`.
    raise NotImplementedError("Complete solve() for White Sheet")


def main():
    # Codeforces: input comes directly from standard input.
    white_sheet = tuple(map(int, input().split()))
    black_sheet1 = tuple(map(int, input().split()))
    black_sheet2 = tuple(map(int, input().split()))

    visible = solve(white_sheet, black_sheet1, black_sheet2)

    # Codeforces expects the literal words YES or NO (uppercase).
    print("YES" if visible else "NO")


if __name__ == "__main__":
    main()
