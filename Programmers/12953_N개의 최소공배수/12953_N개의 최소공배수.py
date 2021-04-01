# 정답 코드 
import math
def solution(arr):
    answer = 1
    if len(arr) == 1:
        return arr[0]
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop() 
        temp_gcd = math.gcd(a, b) 
        temp_lcd = (a * b) // temp_gcd
        arr.append(temp_lcd)
    return arr[0]

# 8개/10개 (틀린 코드)
def solution(arr):
    answer = 1
    while True:
        for i in range(2, max(arr)+1):
            flag = False
            for j in range(len(arr)):
                if arr[j] % i == 0:
                    flag = True
                    arr[j] = arr[j] // i 
            if flag:
                answer *= i
        if sum(arr) == len(arr):
            break
    return answer