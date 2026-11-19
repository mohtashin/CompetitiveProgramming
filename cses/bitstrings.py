input = int(input())
MOD = 10**9 + 7
output = 1
for i in range(input):
    output = 2 * output
    output = output % MOD


print(output)
