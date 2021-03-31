import math
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