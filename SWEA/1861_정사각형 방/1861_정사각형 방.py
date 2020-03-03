def find_num(x, y):
    count = 1
    for k in range(4):
        current_x = x + dx[k]
        current_y = y + dy[k]
        if 0<= current_x <N and 0<=current_y <N and arr[x][y]+1 == arr[current_x][current_y]:
            count += find_num(current_x, current_y)
    else:
        return count


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    start_num = 0

    for i in range(N):
        for j in range(N):
            counter = find_num(i, j)
            if counter > max_count:
                max_count = counter
                start_num = arr[i][j]
            elif counter == max_count:
                if start_num > arr[i][j]:
                    start_num = arr[i][j]

    print('#{} {} {}'.format(tc, start_num, max_count))

