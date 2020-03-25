import sys
sys.setrecursionlimit(1000000)
di=[1,0,-1,0]
dj=[0,1,0,-1]

N,M= map(int, sys.stdin.readline().split())

data=[x.rstrip().split() for x in sys.stdin.readlines()]

max_safe_size=0
def make_wall(start,left_to_pick):
    global max_safe_size
    if left_to_pick==0:
        temp=[row[:] for row in data]
        safe_size=check_safe_size(temp)
        if safe_size>max_safe_size:
            max_safe_size=safe_size
    else:
        for idx in range(start,N*M):
            i=idx // M 
            j=idx % M 
            if data[i][j] == '0':
                data[i][j]='1'
                make_wall(idx+1,left_to_pick-1)
                data[i][j]='0'

def check_safe_size(matrix):
    cnt=0
    ########count virus spreaded area#####
    def dfs(i,j):
        nonlocal cnt
        cnt+=1
        matrix[i][j]='3'
        for k in range(4):
            ni=i+di[k]
            nj=j+dj[k]
            if 0<=ni<N and 0<=nj<M and matrix[ni][nj]=='0':
                matrix[ni][nj]='3'
                dfs(ni,nj)
    
    ########check '1' size######
    wall_size= sum([row.count('1') for row in matrix])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='2':
                dfs(i,j)
    
    result=len(matrix)*len(matrix[0])-wall_size-cnt
    return result

make_wall(0,3)
print(max_safe_size)