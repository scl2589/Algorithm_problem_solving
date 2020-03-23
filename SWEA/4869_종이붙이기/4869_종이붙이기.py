F = [0] * 31
F[1] = 1
F[2] = 3

for i in range(3, 31):
    F[i] = F[i-1]+F[i-2]*2
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())//10
    print('#{} {}'.format(tc, F[N]))    
