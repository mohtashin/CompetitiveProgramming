# n = int(input())
# str_nums = input()

n = 4
str_nums = "1 1 2 3"

nums = list(map(int, str_nums.split()))
num_total = 0

left = [0] * n
right = [0] * n

total = 0
for i in range(n):
    left[i] = total
    total += nums[i]

num_total = total

total = 0

for i in range(n - 1, -1, -1):
    right[i] = total
    total += nums[i]

print(num_total)
print(left)
print(right)

# loop through i - j

for i in range(n):
    for j in range(i, n):
        width = j - i
