#정답을 한꺼번에 출력시켜줘야 한다. 그래야 속도가 월등히 빠르다.
T = int(input())
ans = []
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())
    if A/B > C/D:
        res = 'ALICE'
    elif A/B==C/D:
        res = 'DRAW'
    else:
        res = 'BOB'
    ans.append(res)

for i in range(T):
    print(f'{i+1} {ans[i]}') 
