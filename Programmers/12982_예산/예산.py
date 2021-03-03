def solution(d, budget):
    answer = 0
    total = 0 
    d.sort() 
    for i in d:
        if total + i <= budget:
            answer += 1
            total += i 
        else:
            return answer
    return answer