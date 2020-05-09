from sys import stdin
#from collections import deque
N, K = map(int, stdin.readline().split())
ppl = list(range(1, N+1))
result = []
temp = K-1
for i in range(N):
    if len(ppl) > temp:
        result.append(ppl.pop(temp))
        temp += K - 1
    else:
        temp %= len(ppl)
        result.append(ppl.pop(temp))
        temp += K - 1
print("<", end= '')
for i in result:
    if i == result[-1]:
        print(i, end='')
    else:
        print('{}, '.format(i), end='')
print(">")
