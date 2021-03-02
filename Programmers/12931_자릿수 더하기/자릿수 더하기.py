def solution(n):
    answer = 0

    word = str(n) 
    for i in word:
        answer += int(i)

    return answer