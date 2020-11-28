x = []
y = []
for _ in range(3):
    i, j = map(int, input().split())
    if i in x:
        x.remove(i)
    else:
        x.append(i)
    if j in y:
        y.remove(j)
    else:
        y.append(j)
print(*x, *y)