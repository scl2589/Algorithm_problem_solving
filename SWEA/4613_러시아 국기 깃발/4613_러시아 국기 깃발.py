for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) #국기의 크기
    arr = [input() for _ in range(N)] #오래된 국기의 색 정보
    
    for i in range(0, N-3+1):
        for j in range(i+1, N-2+1):
            cnt = 0
            #흰색 영역: 0~i까지
            for r in range(0, i+1):
                for c in range(M):
                    if arr[r][c]!='W': cnt +=1
            #파란색: i+1~j까지
            for r in range(i+1, j+1):
                for c in range(M):
                    if arr[r][c] != 'B': cnt += 1
                        
            #빨간색: j+1, N-1까지
            for r in range(j+1, N):
                for c in range(M):
                    if arr[r][c] != 'R': cnt += 1
                       
            ans = min(ans, cnt)
                
                