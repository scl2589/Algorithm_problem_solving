T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M):
        print(lst.insert(*map(int, input().split())) )
    print('#{} {}'.format(tc, lst[L]))