import sys

first_line = sys.stdin.readline().strip()
new_lst = first_line.split()
new_lst = list(map(int, new_lst))
sorted_lst = sorted(new_lst)
abc = max(new_lst)
a = min(new_lst)
bc = abc - a
b = sorted_lst[1]
c = bc - b
print(f"{a} {b} {c}")
