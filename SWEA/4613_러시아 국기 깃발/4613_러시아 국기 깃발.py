#아직 미완성
arr = [1,2,3,4,5]; N = len(arr)
for i in range(0, N-3+1):
    for j in range(i+1, N-2+1):
        print(arr[:i+1], end='')
        print(arr[i+1:j+1], end='')
        print(arr[j+1:N], end='')
        print()