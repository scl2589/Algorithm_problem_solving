from collections import Counter
def solution(number, k):
    answer = Counter(list(number))
    answer = sorted(answer.items(), key = lambda x : x[0])
    total = k
    for idx, i in enumerate(answer):
        if i[1] >= k:
            number = number.replace(i[0], '', k)
            break
        else:
            number = number.replace(i[0], '', i[1])
            k = k - i[1]
    return number