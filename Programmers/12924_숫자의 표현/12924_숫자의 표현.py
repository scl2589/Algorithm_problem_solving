def solution(n):
    count = 0
    for i in range(1, n+1):
        total = 0
        for j in range(i, n+1):
            total += j
            if total > n:
                break 
            elif total == n:
                count += 1
                break 
                
    return count