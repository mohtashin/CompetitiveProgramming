n = int(input())
count = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count += 1

print(count)


# w = input()
# rows = int(w[0])
# count = 0
# i = 0
# for lines in w.splitlines():
#     if i == 0:
#         i += 1
#         continue
#     sum = int(lines[0]) + int(lines[2]) + int(lines[4])
#     if sum >= 2:
#         count += 1
#     i += 1
# print(count)
