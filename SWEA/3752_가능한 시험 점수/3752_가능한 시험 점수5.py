T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(int, input().split()) #문제별 점수
    total = sum(p)
    s = [0] * (total + 1)
    s[0] = 1
    
    for x in p: #x점 문제에 대해
        for i in range(total-x, -1, -1):
            if s[i] == 1: #i점이 가능하면
                s[i+x]== 1 #i+x점도 가능
                
    print('#{} {}'.format(tc, sum(s))) #가능한 점수의 개수 출력