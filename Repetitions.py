line = input()
count = 1
max = 1
for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        count += 1
        if count > max:
            max = count
    elif line[i] != line[i - 1]:
        count = 1
        if count > max:
            max = count

print(max)
