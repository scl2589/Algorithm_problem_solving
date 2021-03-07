n = int(input())
arr = [0]
for i in range(1, n+1):
    if i == 1:
        arr.append(1)
    elif i == 2:
        arr.append(2)
    else:
        arr.append(arr[-1] + arr[-2])
print(arr[n] % 10007)