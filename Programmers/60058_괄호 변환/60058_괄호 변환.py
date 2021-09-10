def isCorrect(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            return False
    return True

def solution(p):
    # 1번
    if len(p) == 0 or isCorrect(p):
        return p
    
    # u가 균형잡힌 괄호 문자열이 될 때 까지 만들기
    u = []
    v = []
    for i in range(2, len(p)+1, 2):
        temp = p[:i]
        if temp.count('(') == temp.count(')'):
            u = temp
            v = p[i:]
            break
    else:
        u = p
        v = ""
    
    # 3번 
    # u가 올바른 문자열이라면 v에 대해 1단계 수행 
    if isCorrect(u): 
        u += solution(v)
        return u
    
    # 4번
    # u가 올바른 문자열이 아니라면 
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        u = u[1:len(u)-1]
        for i in u:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        return temp 
    