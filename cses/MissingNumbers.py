l1 = input()
l2 = input().split(" ")
l2 = set(l2)
for i in range(1, int(l1) + 1):
    if str(i) in l2:
        pass
    else:
        print(i)
