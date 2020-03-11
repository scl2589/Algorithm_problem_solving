for tc in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split()) #x1, y1
    
    ans = 0
    for _ in range(N-1): #N-1 개의 좌표를 입력받는다.
        tx, ty = map(int, input().split())
        if x == tx:
            ans += abs(y-ty) #수직 이동
        elif y == ty:
            ans += abs(x-tx) #수평 이동
        elif (x < tx and y > ty) or (x > tx and y < ty):
            ans += abs(x- tx) + abs(y-ty)
        else: #우상에서 좌하로 가는 경우
            ans += max(abs(x-tx), abs(y-ty))
            
        x , y = tx, ty
            
            
    print('#{} {}'.format(tc, ans))



