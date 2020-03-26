def shoot(y, x):
    tmin = 1e9
    xx = yy = -1

for i in range(y-1, -1, -1):
    for j in range(M):
        if mat[i][j] and not killed[i][j]:
            t = abs(i-y) + abs(j-x)
            if t < tmin:
                tmin, xx, yy = t, j, i
            elif t==tmin and xx > j:
                xx, yy = j, i
return (tmin<=D, xx, yy)
def attack(archor):
    t = []
    for pos in range(N, 0, -1):
        t.append(shoot(pos, archor[0]))
        t.append(shoot(pos, archor[1]))
        t.append(shoot(pos, archor[2]))

    for p in t:
        if p[0]:
            killed[p[2]][p[1]] = 1
N, M, D = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
archor = [0]*3

tmax = 0
for k0 in range(0, M-2):
    for k1 in range(k0+1, M-1):
        for k2 in range(k1+1, M):
            killed = [[0]*M for _ in range(N)]
            archor[0], archor[1], archor[2] = k0, k1, k2
            attack(archor)
            tmax = max(tmax, sum(sum(killed, [])))
print(tmax)