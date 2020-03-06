#Fail (Runtime error)
'''
시간초과 이유는 중복 숫자가 있어도 계속 저장해놓기 때문에, 리스트의 크기가 커지면서 메모리의 크기가 커진다.
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = list(int, input().split()) #문제별 점수
    ans = [0] #0점인 경우
    
    for x in p: #문제별 점수
        num = []
        for y in ans: #가능한 점수
            num.append(x+y)
        ans += num
    print('#{} {}'.format(tc, len(set(ans))))    