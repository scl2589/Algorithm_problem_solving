T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    lenA = len(A)
    lenB = len(B)
    i = 0
    count = 0
    while i < len(A):
        if A[i:i+len(B)]==B:
            count += 1
            i += len(B)
        else:
            count += 1
            i += 1
    print('#{} {}'.format(tc, count))
        
