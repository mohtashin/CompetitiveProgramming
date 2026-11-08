l1 = int(input())
l2 = input()
l2 = list(map(int, l2.split(" ")))
count = 0
for i in range(1, l1):
    if l2[i] < l2[i - 1]:
        calc = l2[i - 1] - l2[i]
        count += calc
        l2[i] += calc
print(count)
