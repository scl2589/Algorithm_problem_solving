# 에라토스테네스의 체 
def solution(n):
    answer = 0
    visit = [True] * (n+1)
    number = int(n**(0.5))
    for i in range(2, number + 1):
        if visit[i] == True:
            for j in range(i*i, n+1, i):
                visit[j] = False 
    
    x = [i for i in range(2, n+1) if visit[i] == True]
    answer = len(x)
    return answer
        
        
    return answer