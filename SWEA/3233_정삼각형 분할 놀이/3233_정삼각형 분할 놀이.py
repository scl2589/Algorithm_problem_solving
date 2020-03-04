T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    quotient = A//B
    print('#{} {}'.format(tc, quotient ** 2))