input = int(input())
if input in [2, 3]:
    print("NO SOLUTION")
elif input == 1:
    print("1")
else:
    res = []
    start = 2
    while start <= input:
        res.append(str(start))
        start += 2

    start = 1
    while start <= input:
        res.append(str(start))
        start += 2
    print(" ".join(res))
