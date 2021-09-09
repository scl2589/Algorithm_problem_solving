def solution(scores):
    answer = []
    
    zipped = list(zip(*scores))
    for idx, lst in enumerate(zipped):
        total = sum(lst)
        len_lst = len(lst)
        if lst[idx] in [max(lst), min(lst)]:
            if lst.count(lst[idx]) == 1:
                total -= lst[idx]
                len_lst -= 1 
        
        final_score = total / len_lst 
        answer.append(grade(final_score))
        
    return "".join(answer)


def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
        