N = int(input())
answer = 1
def factorial(n):
    global answer
    if n <= 1:
        print(answer)
    else:
        answer *= n
        factorial(n-1) 

factorial(N)