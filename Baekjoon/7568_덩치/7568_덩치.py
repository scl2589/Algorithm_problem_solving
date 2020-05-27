N = int(input())
tables = [list(map(int, input().split())) for _ in range(N)]

for i in tables:
    rank = 1
    for j in tables:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end=' ')