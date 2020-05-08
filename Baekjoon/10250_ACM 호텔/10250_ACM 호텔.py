T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    # 맨 마지막 방의 손님이면 층수를 꼭대기 층으로 설정한다.
    if N % H == 0:
        floor = H
        num = N // H
    else:
        floor = N % H
        num = N // H  + 1
    if num < 10:
        print(str(floor)+'0'+str(num))
    else:
        print(str(floor)+str(num))