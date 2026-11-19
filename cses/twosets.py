input = int(input())
count = 0
n = input
while n != 0:
    count += n
    n -= 1
if count % 2 != 0:
    print("NO")

else:
    target = count // 2  # 33
    set1count = 0  # 11 21 30
    set1list = []  # 11 10 9 3
    set2list = []  # 8 7 6 5 4

    for i in range(input, 0, -1):  # 1 2 3 4 5 6 7 8 9 10 11
        if set1count + i <= target:
            set1count += i
            set1list.append(i)
        else:
            set2list.append(i)

    print("YES")
    print(len(set1list))
    print(" ".join(map(str, set1list)))
    print(len(set2list))
    print(" ".join(map(str, set2list)))
