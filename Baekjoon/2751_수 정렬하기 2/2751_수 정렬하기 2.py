'''
import sys
N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(input()))
for i in sorted(num):
    sys.stdout.write(str(i)+'\n')
'''

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num = sorted(num)
for i in num:
    print(i)


