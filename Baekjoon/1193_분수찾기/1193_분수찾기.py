# 규칙을 찾자면
# 짝수일때는 분모 -1 / 분자 + 1
# 홀수일때는 분모 + 1/ 분자 - 1
N = int(input())
count = 0

while N > 0:
    N -= count 
    count +=1 

N = count + N - 1

ans = str(N) + '/' + str(count - N)
if count % 2 == 0:
    ans = str(count - N) + '/' + str(N)

print(ans)