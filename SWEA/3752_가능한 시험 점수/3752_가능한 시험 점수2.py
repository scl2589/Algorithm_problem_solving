T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(int, input().split()) #문제별 점수
    ans = set([0]) #0점인 경우
    
    for x in p: #문제별 점수
        num = set()
        for y in ans: #가능한 점수
            num.append(x+y)
        ans = set(list(ans)+list(num))
    print('#{} {}'.format(tc, len(set(ans))))    