#내 풀이
for tc in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    x1, y1 = map(int, input().split())
    coordinates = [list(map(int, input().split())) for _ in range(N-1)]
    result = 0
    
    for i in range(len(coordinates)):
        x2, y2 = coordinates[i][0], coordinates[i][1]
        diff_x = x1 - x2
        diff_y = y1 - y2
        
        if diff_x * diff_y <0 : #좌상에서 우하로 이동할 경우
            result += abs(diff_x) + abs(diff_y)
        else:
            result += max(abs(diff_x), abs(diff_y))
        x1, y1 = x2, y2
            
    print('#{} {}'.format(tc, result))

