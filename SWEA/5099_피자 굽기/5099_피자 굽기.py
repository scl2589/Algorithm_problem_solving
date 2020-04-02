T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    q2 = [(x, i) for i, x in enumerate(q, start=1)]
    subQ = [q2.pop(0) for _ in range(N)]
    while len(subQ) != 1:
        temp = subQ.pop(0)
        num = temp[0]//2
        if num:
            subQ.append((num, temp[1]))
        else:
            if q2:
                tempQ = q2.pop(0)
                subQ.append((tempQ[0], tempQ[1]))
    print('#{} {}'.format(tc, subQ[0][1]))
