def powerset(n, d, total): #d: depth
    global minV, B
    if total == B:
        minV = 0
    elif total > B:
        minV = min(total - B, minV)
        return
    elif n == d:
        return
    else:
        A[d] = 1
        powerset(n, d+1, total+heights[d])
        A[d] = 0
        powerset(n, d+1, total)



T = int(input())
for tc in range(1, T+1):
    # N= 점원 수 #B: 선반 높이
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    minV = float('inf')
    A = [0] * (N)
    powerset(N, 0, 0)
    print(f'#{tc} {minV}')
    

