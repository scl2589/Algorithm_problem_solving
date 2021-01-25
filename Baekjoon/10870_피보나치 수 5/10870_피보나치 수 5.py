N = int(input())
count = 2
arr = [0, 1]
def fib(n1, n2):
    global count
    if count == N+1:
        print(arr[count-1])
    else:
        arr.append(n1+n2)
        count += 1
        fib(arr[count-2], arr[count-1])
if N == 0:
    print(arr[0])
else:
    fib(arr[0], arr[1])