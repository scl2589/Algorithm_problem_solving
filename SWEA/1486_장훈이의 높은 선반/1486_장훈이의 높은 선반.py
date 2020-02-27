from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    combi = []
    min_num = 0
    for i in range(1,N+1):
        temp = combinations(heights, i)
        for j in temp:
            if sum(j) >= B:
                if not combi:
                    min_num = sum(j)
                    combi.append(j)
                else:
                    if sum(j) < min_num:
                        min_num = sum(j)
                        combi.append(j)
    print('#{} {}'.format(tc, min_num-B))
