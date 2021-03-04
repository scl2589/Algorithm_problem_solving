import itertools
def solution(nums):
    biggest = sum(nums)
    n = [i for i in range(1, biggest + 1)]
    
    # 에라토스테네스의 체 
    m = int(biggest**(0.5)) + 1
    visit = [True] * (biggest + 1)
    for i in range(2, m):
        for j in range(i*i, biggest + 1, i):
            if visit[j] == True: 
                visit[j] = False
    prime = [i for i in range(1, biggest + 1) if visit[i]]

    # 3가지 숫자의 합 확인 
    answer = 0
    comb = list(itertools.combinations(nums, 3))
    for each in comb:
        if sum(each) in prime:
            answer += 1
    return answer

'''
테스트 1 〉	통과 (3.83ms, 10.4MB)
테스트 2 〉	통과 (5.54ms, 10.4MB)
테스트 3 〉	통과 (1.17ms, 10.3MB)
테스트 4 〉	통과 (0.95ms, 10.3MB)
테스트 5 〉	통과 (6.07ms, 10.4MB)
테스트 6 〉	통과 (43.56ms, 10.8MB)
테스트 7 〉	통과 (2.42ms, 10.3MB)
테스트 8 〉	통과 (103.60ms, 11.5MB)
테스트 9 〉	통과 (6.18ms, 10.5MB)
테스트 10 〉	통과 (105.43ms, 11.3MB)
테스트 11 〉	통과 (1.27ms, 10.1MB)
테스트 12 〉	통과 (0.09ms, 10.3MB)
테스트 13 〉	통과 (0.21ms, 10.3MB)
테스트 14 〉	통과 (0.09ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.3MB)
테스트 16 〉	통과 (352.98ms, 12.1MB)
테스트 17 〉	통과 (518.84ms, 12.7MB)
테스트 18 〉	통과 (2.17ms, 10.5MB)
테스트 19 〉	통과 (1.19ms, 10.3MB)
테스트 20 〉	통과 (479.26ms, 12.7MB)
테스트 21 〉	통과 (390.07ms, 12.3MB)
테스트 22 〉	통과 (64.01ms, 11MB)
테스트 23 〉	통과 (0.03ms, 10.4MB)
테스트 24 〉	통과 (334.71ms, 12.2MB)
테스트 25 〉	통과 (341.09ms, 12.1MB)
테스트 26 〉	통과 (0.02ms, 10.1MB)
'''

# 더 빠른 풀이

def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

'''
테스트 1 〉	통과 (3.06ms, 10.2MB)
테스트 2 〉	통과 (4.14ms, 10.1MB)
테스트 3 〉	통과 (1.14ms, 10.2MB)
테스트 4 〉	통과 (0.79ms, 10.2MB)
테스트 5 〉	통과 (3.80ms, 10.2MB)
테스트 6 〉	통과 (24.48ms, 10.2MB)
테스트 7 〉	통과 (1.21ms, 10.1MB)
테스트 8 〉	통과 (42.65ms, 10.1MB)
테스트 9 〉	통과 (4.56ms, 10.1MB)
테스트 10 〉	통과 (43.13ms, 10.2MB)
테스트 11 〉	통과 (0.18ms, 10.2MB)
테스트 12 〉	통과 (0.08ms, 10.3MB)
테스트 13 〉	통과 (0.19ms, 10.2MB)
테스트 14 〉	통과 (0.08ms, 10.2MB)
테스트 15 〉	통과 (0.07ms, 10.2MB)
테스트 16 〉	통과 (139.60ms, 10.2MB)
테스트 17 〉	통과 (8.17ms, 10.3MB)
테스트 18 〉	통과 (2.17ms, 10.1MB)
테스트 19 〉	통과 (0.25ms, 10MB)
테스트 20 〉	통과 (190.88ms, 10.2MB)
테스트 21 〉	통과 (164.87ms, 10.2MB)
테스트 22 〉	통과 (1.98ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (142.59ms, 10.2MB)
테스트 25 〉	통과 (145.36ms, 10.3MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
'''

# 더 빠른 풀이
from itertools import combinations
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])

'''
테스트 1 〉	통과 (3.55ms, 10.3MB)
테스트 2 〉	통과 (4.98ms, 10.3MB)
테스트 3 〉	통과 (1.27ms, 10.2MB)
테스트 4 〉	통과 (1.02ms, 10.2MB)
테스트 5 〉	통과 (6.52ms, 10.3MB)
테스트 6 〉	통과 (9.76ms, 10.2MB)
테스트 7 〉	통과 (0.55ms, 10.3MB)
테스트 8 〉	통과 (21.41ms, 10.4MB)
테스트 9 〉	통과 (2.98ms, 10.1MB)
테스트 10 〉	통과 (20.70ms, 10.3MB)
테스트 11 〉	통과 (0.21ms, 10.3MB)
테스트 12 〉	통과 (0.11ms, 10.2MB)
테스트 13 〉	통과 (0.27ms, 10.2MB)
테스트 14 〉	통과 (0.11ms, 10.2MB)
테스트 15 〉	통과 (0.10ms, 10.2MB)
테스트 16 〉	통과 (32.19ms, 10.3MB)
테스트 17 〉	통과 (41.93ms, 10.4MB)
테스트 18 〉	통과 (0.36ms, 10.2MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (40.90ms, 10.4MB)
테스트 21 〉	통과 (36.77ms, 10.4MB)
테스트 22 〉	통과 (8.36ms, 10.3MB)
테스트 23 〉	통과 (0.02ms, 10.2MB)
테스트 24 〉	통과 (31.41ms, 10.4MB)
테스트 25 〉	통과 (32.36ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
'''

# 제일 빠른 풀이

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
def solution(nums):
    import itertools
    n_list = list(sum(i) for i in itertools.combinations(nums, 3))
    n_doc = {}
    for i in n_list:
        if i not in n_doc.keys():
            n_doc[i] = 1
        else:
            n_doc[i] += 1
    n_set = set(n_doc.keys())
    n_max = max(n_set)
    for i in range(2, int(n_max**0.5 + 1)):
        n_set -= set(range(2*i, n_max+1, i))
    answer = 0
    for i in n_set:
        answer += n_doc[i]
    return answer
'''
테스트 1 〉	통과 (1.40ms, 10.3MB)
테스트 2 〉	통과 (1.85ms, 10.3MB)
테스트 3 〉	통과 (0.41ms, 10.3MB)
테스트 4 〉	통과 (0.33ms, 10.3MB)
테스트 5 〉	통과 (1.84ms, 10.3MB)
테스트 6 〉	통과 (2.59ms, 10.4MB)
테스트 7 〉	통과 (0.38ms, 10.3MB)
테스트 8 〉	통과 (5.74ms, 10.6MB)
테스트 9 〉	통과 (0.96ms, 10.4MB)
테스트 10 〉	통과 (5.57ms, 10.7MB)
테스트 11 〉	통과 (0.09ms, 10.3MB)
테스트 12 〉	통과 (0.12ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.3MB)
테스트 16 〉	통과 (6.59ms, 11MB)
테스트 17 〉	통과 (7.67ms, 11.1MB)
테스트 18 〉	통과 (0.90ms, 10.3MB)
테스트 19 〉	통과 (0.83ms, 10.2MB)
테스트 20 〉	통과 (7.86ms, 11.1MB)
테스트 21 〉	통과 (7.60ms, 11.2MB)
테스트 22 〉	통과 (2.22ms, 10.5MB)
테스트 23 〉	통과 (0.03ms, 10.3MB)
테스트 24 〉	통과 (6.95ms, 11MB)
테스트 25 〉	통과 (6.44ms, 10.9MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
'''