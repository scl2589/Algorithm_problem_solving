# a가 1인 경우를 조심하기 
a = int(input())
b = int(input())

available = []
if a == 1:
    a = 2

for i in range(a, b+1):
    prime = False
    for j in range(2, i):
        if i % j == 0:
            prime = True 
            break
    if prime:
        continue
    else:
        available.append(i)
if available:
    print(sum(available))
    print(available[0])
else:
    print(-1)