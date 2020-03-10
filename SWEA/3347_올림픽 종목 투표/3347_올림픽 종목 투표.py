for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    voted = [0] * len(A)
    for i in B:
        for j in range(len(A)):
            if i >= A[j]:
                voted[j] += 1
                break
    print('#{} {}'.format(tc, voted.index(max(voted))+1))

