N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
coords = sorted(coords, key = lambda x: (x[1], x[0]))
for i in coords:
    print(i[0], i[1])