def f(n, atom):
    s = 0
    for x in range(4001): #0.5초를 1로 바꾼 후 최대 이동시간
        col = {}
        for i in range(N):
            if atom[i][3] != 0:
                atom[i][0] += dx[atom[i][2]] #이동 후 좌표
                atom[i][1] += dy[atom[i][2]]
                if abs(atom[i][0]) <= 2000 and abs(atom[i][1]) <= 2000:
                    if (atom[i][0], atom[i][1]) not in col: # 좌표 key가 없으면
                        col[(atom[i][0], atom[i][1])] = i # 원소 번호 value
                    else: # 좌표 key가 있으면 충돌로 처리
                        s += atom[col[(atom[i][0], atom[i][1])]][3] + atom[i][3]
                        atom[i][3] = 0
                        atom[col[(atom[i][0], atom[i][1])]][3] = 0
    return s


#이동 방향 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    atom = []
    for i in range(N):
        x, y, d, e = map(int, input().split())
        atom.append([x*2, y*2, d, e])
    ans = f(N, atom)
    print('#{} {}'.format(tc, ans))