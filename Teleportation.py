fin = open("teleport.in", "r")
w = fin.readline().strip()
fin.close()

a, b, x, y = map(int, w.split())
# dont use teleport
cost = abs(a - b)
# go a to x and then y to b
xteley = abs(a - x) + abs(b - y)
if xteley < cost:
    cost = xteley
# go a to y and then x to b
ytelex = abs(a - y) + abs(b - x)
if ytelex < cost:
    cost = ytelex

fout = open("teleport.out", "w")
fout.write(str(cost) + "\n")
fout.close()
