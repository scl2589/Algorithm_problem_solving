from itertools import permutations
def solution(numbers):
    arr = []
    for i in range(1, len(numbers)+1):
        arr.extend(list(permutations(numbers, i)))
    arr = set(int(''.join(i)) for i in arr)
    # print(arr)
    max_arr = max(arr)
    # 에라토스테네스의 체
    m = int(max_arr ** 0.5) + 1
    check = [True] * (max_arr+1) 
    for i in range(2, m):
        for j in range(i*i, max_arr+1, i):
            if check[j] == True:
                check[j] = False
    check[0], check[1] = False, False
    prime_list = []
    for idx, val in enumerate(check):
        if val == True:
            prime_list.append(idx) 
    # print(prime_list)
    answer = 0
    for i in arr:
        if i in prime_list:
            answer += 1
            # print(i)
    return answer

'''
테스트 1 〉	통과 (1.31ms, 10.5MB)
테스트 2 〉	통과 (1264.11ms, 17.7MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (114.59ms, 13.8MB)
테스트 5 〉	통과 (2083.09ms, 45.4MB)
테스트 6 〉	통과 (0.05ms, 10.5MB)
테스트 7 〉	통과 (1.27ms, 10.5MB)
테스트 8 〉	통과 (3375.95ms, 67.9MB)
테스트 9 〉	통과 (0.15ms, 10.5MB)
테스트 10 〉	통과 (1527.87ms, 21.2MB)
테스트 11 〉	통과 (58.74ms, 11.5MB)
테스트 12 〉	통과 (21.15ms, 10.9MB)
'''

'''
빠른 코드
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

테스트 1 〉	통과 (0.94ms, 10.4MB)
테스트 2 〉	통과 (77.90ms, 44.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (53.08ms, 19.9MB)
테스트 5 〉	통과 (261.88ms, 145MB)
테스트 6 〉	통과 (0.05ms, 10.4MB)
테스트 7 〉	통과 (0.92ms, 10.4MB)
테스트 8 〉	통과 (698.75ms, 280MB)
테스트 9 〉	통과 (0.09ms, 10.4MB)
테스트 10 〉	통과 (351.92ms, 51.1MB)
테스트 11 〉	통과 (26.98ms, 13.8MB)
테스트 12 〉	통과 (5.13ms, 13.2MB)
'''

# default dict 사용한 코드
from itertools import permutations
from collections import defaultdict

def is_prime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1

def solution(numbers):
    count = 0
    history = []
    for n in range(len(numbers)):
        for digit_arr in permutations(numbers, n+1):
            number = 0

            for i, digit in enumerate(digit_arr):
                b = len(digit_arr) - i - 1
                number += int(digit) * (1*(10**b))

            if number not in history and is_prime(number):
                history.append(number)
                count+=1

    return count
