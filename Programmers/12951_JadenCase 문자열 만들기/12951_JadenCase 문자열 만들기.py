def solution(s):
    splitted = s.split(' ')
    for idx, i in enumerate(splitted):
        splitted[idx] = i.capitalize() 
    return ' '.join(splitted)