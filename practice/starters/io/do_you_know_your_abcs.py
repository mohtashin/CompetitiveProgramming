"""USACO 2020 December Bronze: Do You Know Your ABCs?

Judge I/O: stdin and stdout (USACO changed to standard I/O in Dec 2020).
"""


def main():

    numbers = list(map(int, input().split()))
    sortedarray = sorted(numbers)
    a = int(sortedarray[0])
    b = int(sortedarray[1])
    c = int(sortedarray[5] - b)

    print(a, b, c)


if __name__ == "__main__":
    main()
