# 좋은 방법은 아니다.

def f1(n): # n번 노드 방문
    global ans 
    if n >= 0:
        if n == 99:
            ans = 1
        f1(ch1[n])
        f1(ch2[n])


for _ in range(10):
    tc, E = map(int, input().split())
    tmp = list(map(int, input().split()))

    # 출발점을 index로 도착점 번호를 저장
    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(E):
        n1 = tmp[i*2] # 출발
        n2 = tmp[i*2 + 1] # 도착

        if ch1[n1] == 0 : # 첫 도착지이면
            ch1[n1] = n2
        else: # 두번째 도착지이면
            ch2[n1] = n2
    ans = 0
    f1(0)
    print(f'#{tc} {ans}')