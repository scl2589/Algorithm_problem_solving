def solution(s):
    answer = ''
    idx = 0
    word = ''
    dict = {
        'zero': 0,
        'one' : 1,
        'two' : 2,
        'three': 3,
        'four' : 4,
        'five' : 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    while idx < len(s):
        if s[idx].isnumeric():
            answer += str(s[idx])
            idx += 1
        else: 
            word += s[idx]
            if word in dict:
                answer += str(dict[word])
                word = ''
            idx += 1
    return int(answer)

'''깔끔쓰
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
'''