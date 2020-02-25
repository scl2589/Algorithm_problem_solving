T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D/(A+B)
    fly_distance = time * F
    print('#{} {}'.format(tc, fly_distance))