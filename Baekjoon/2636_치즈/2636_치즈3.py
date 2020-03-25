import sys
from collections import deque
sys.setrecursionlimit(1000000)
N,M = map(int, sys.stdin.readline().rstrip().split())


cheeze= [ sys.stdin.readline().rstrip().split() for _ in range(N)]

di=[1,0,-1,0]
dj=[0,1,0,-1]

def make_outside_two(i,j):
    cheeze[i][j]='2'

    for k in range(4):
        ni=i+di[k]
        nj=j+dj[k]
        if 0<=ni<N and 0<=nj<M and cheeze[ni][nj]=='0':
            make_outside_two(ni,nj)

def melt():
    surround=[[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            cnt=0
            for k in range(4):
                ni=i+di[k]
                nj=j+dj[k]
                if 0<=ni<N and 0<=nj<M and cheeze[ni][nj]=='2':
                    cnt+=1
            surround[i][j]=cnt

    for i in range(N):
        for j in range(M):
            if surround[i][j] != 0 and cheeze[i][j]=='1':
                cheeze[i][j]='2'

    for i in range(N):
        for j in range(M):
            if cheeze[i][j]=='0':
                for k in range(4):
                    ni=i+di[k]
                    nj=j+dj[k]
                    if 0<=ni<N and 0<=nj<M and cheeze[ni][nj]=='2':
                        make_outside_two(i,j)



t=0
make_outside_two(0,0)
while cheeze != [['2']*M for _ in range(N)]:
    before= sum([ row[:].count('1') for row in cheeze])
    melt()
    t+=1

print(t)
print(before)