T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 화덕의 크기, M = 피자 개수
    Ci = list(map(int, input().split()))
    Ci = list(enumerate(Ci, start=1)) # 피자번호, 치즈
 
    baking = []
    for _ in range(N):
        baking.append(Ci.pop(0))
 
    while len(baking) != 1:
        pizza = list(baking.pop(0))
        pizza[1] //= 2
        if pizza[1]:
            baking.append(pizza)
        else:
            if Ci:
                baking.append(Ci.pop(0))
 
    print(f'#{tc} {baking[0][0]}')
