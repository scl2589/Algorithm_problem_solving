S= [int(i) for i in list(input())]
count0 = 0
count1 = 0

# 첫 번째 원소에 대해서 처리
if S[0] == 0:
    count1 = 1
else: 
    count0 = 1

for i in range(1, len(S)):
    if S[i-1] != S[i]:
        # 다음 수가 0인 경우, 1로 바꿔준다.
        if S[i] == 0:
            count1 += 1
        # 다음 수가 1인 경우, 0으로 바꿔준다.
        else:
            count0 += 1
print(min(count1, count0))