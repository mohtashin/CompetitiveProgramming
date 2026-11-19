import sys

#sys.stdin = open("traffic.in", "r")
#sys.stdout = open("traffic.out", "w")


def solve():
    # STEP 1: Read the number of road segments
    n = int(input())

    # STEP 2: Read each sensor type and its low/high readings
    sensors = []
    start_low = 0
    start_high = 1000
    _ = 0
    firstnone = 0
    lastnone = 0
    while _ < n:#
        kind, low, high = input().split()
        sensors.append((kind, int(low), int(high)))
        if kind == "none":
            if firstnone == 0:
                firstnone = _
            lastnone = _

        if kind == "none" and int(low) >= int(start_low):
            start_low = int(low)
        if kind == "none" and int(high) <= int(start_high):
            start_high = int(high)
        _ += 1
    end_low = start_low
    end_high = start_high
    # STEP 3: TODO - Find the possible traffic range at the start

    for i in range(lastnone):
        if sensors[i][0] == "on":
            start_low -= sensors[i][2]
            start_high -= sensors[i][1]
        if sensors[i][0] == "off":
            start_low += sensors[i][2]
            start_high += sensors[i][1]
    # STEP 4: TODO - Find the possible traffic range at the end
    for i in range(firstnone, len(sensors)):
        if sensors[i][0] == "on":
            end_low += sensors[i][2]
            end_high += sensors[i][1]
        if sensors[i][0] == "off":
            end_low -= sensors[i][2]
            end_high -= sensors[i][1]
    # STEP 5: Output the two ranges (one range per line)
    print(start_low, start_high)
    print(end_low, end_high)


if __name__ == "__main__":
    solve()
