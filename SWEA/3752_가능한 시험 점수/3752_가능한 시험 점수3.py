T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    chk = [True] + [False for _ in range(total)]
    for i in a:
        for j in range(total, -1, -1):
            if chk[j]:
                chk[j+i] = True
    print("#{} {}".format(t, sum(chk)))