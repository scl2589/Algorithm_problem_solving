from collections import deque

tc = int(input())

for _ in range(tc):
    N, M = map(int, input().split())
    impt = list(map(int, input().split()))

    q = deque() 
    for idx, value in enumerate(impt):
        q.append([idx, value])

    count = 0

    while True:
        max_num = sorted(q, key = lambda x: x[1], reverse=True)[0][1]
        num = q.popleft()
        if num[0] == M and num[1] == max_num:
            break 
        elif num[1] == max_num:
            count += 1
        else:
            q.append(num)
    print(count + 1)

