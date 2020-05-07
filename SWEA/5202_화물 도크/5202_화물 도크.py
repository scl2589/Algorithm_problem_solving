for tc in range(1, int(input())+1):
    N = int(input())
    timetable = []
    for _ in range(N):
        timetable.append(tuple(map(int, input().split())))
    
    timetable.sort(key=lambda x: x[1])
    end = timetable[0][0]
    cnt = 1
    for i in range(1, N):
        if end <= timetable[i][0]:
            end = timetable[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))
    