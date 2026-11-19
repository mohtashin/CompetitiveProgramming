# k + 2k + 3k + 4k ...1 , 2, 3, w
# input = 3 17 4
# 3 + 6 + 9 + 12 = 30
# 30-17=13
# w = 4
my_lst = input().split()  # [k, n, w]

cost = 0
for i in range(int(my_lst[2])):
    cost += int(my_lst[0]) * (i + 1)

ans = max(0, cost - int(my_lst[1]))
print(ans)
