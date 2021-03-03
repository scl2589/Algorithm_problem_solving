from math import gcd 
def solution(n, m):
    answer = []
    
    # n과 m 중에 더 큰 수를 m으로 만든다.
    if m < n:
        m, n = n, m
    # gcd를 찾기 위한 변수이다.
    gcd = 0 
    
    # 1부터 m까지 
    for i in range(1, m+1):
        # n과 m이 모두 i로 나눠지면 공약수이다. 
        if n % i == 0 and m % i == 0:
            # 공약수라면 gcd를 갱신해준다. 
            gcd = i 
    # 가장 마지막 공약수가 최대공약수이므로 answer에 추가!
    answer.append(gcd)
    # 최소 공배수는 최대공약수 * 각 숫자를 최대공약수로 나눈 값을 곱한 값이다. 
    answer.append(gcd * n // gcd * m // gcd)
    
    # 최소공배수 구하기 
    return answer