n = int(input())
print(str(n) + " ")
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
        print(str(n) + " ")
    elif n % 2 == 1:
        n = int(n * 3 + 1)
        print(str(n) + " ")
