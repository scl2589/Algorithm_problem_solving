T = int(input())
check = [True] * (10**6+1)
for i in range(2, 10**6+1):
    if check[i]:
        for j in range(i * 2, 10**6+1, i):
            check[j] = False

for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    count = 0
    for i in range(A, B+1):
        if i>= 2 and check[i] and str(D) in str(i):
            count += 1
    print('#{} {}'.format(tc, count))

