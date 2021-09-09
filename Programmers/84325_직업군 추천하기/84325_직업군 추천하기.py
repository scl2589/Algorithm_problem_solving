def solution(table, languages, preference):
    answer = ''
    answer_list = []
    for t in table:
        lst = t.split(' ')
        new = [lst[0]]
        new.extend(lst[5:0:-1])
        total = 0
        for idx, language in enumerate(languages):
            if language in new:
                total += new.index(language) * preference[idx]
        answer_list.append([total, new[0]])
    answer_list = sorted(answer_list, key = lambda x : (-x[0], x[1]))
    return answer_list[0][1]