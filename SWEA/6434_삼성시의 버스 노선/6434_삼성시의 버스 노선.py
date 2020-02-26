import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #버스노선의 개수다

    numOfBus = [0 for _ in range(5000)]
    selected_station = []

    for _ in range(N):
        a, b = map(int, input().split())
        #a에서 b까지 방문한 버스 정류장
        for i in range(a, b+1):
            numOfBus[i-1] += 1

    P = int(input())#버스 정류장 개수
    for _ in range(P):
        station = int(input())
        selected_station.append(str(numOfBus[station-1]))

    print('#{} {}'.format(tc, ' '.join(selected_station)))