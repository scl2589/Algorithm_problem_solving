word = input()
count = 0
alphabet= {
    'c=':0,
    'c-':0,
    'dz=':0,
    'd-':0,
    'lj':0,
    'nj':0,
    's=':0,
    'z=':0,
}
i = 0
while i < len(word)-1:
    flag = False
    flag2 = False
    if word[i:i+2] == 'c=':
        alphabet['c='] +=1
    elif word[i:i+2] == 'c-':
        alphabet['c-'] +=1
    elif word[i:i+2] == 'dz':
        if i + 3 <= len(word) and word[i:i+3] == 'dz=':
            alphabet['dz='] +=1
            flag = True
    elif word[i:i+2] == 'd-':
        alphabet['d-'] +=1
    elif word[i:i+2] == 'lj':
        alphabet['lj'] +=1
    elif word[i:i+2] == 'nj':
        alphabet['nj'] +=1
    elif word[i:i+2] == 's=':
        alphabet['s='] +=1
    elif word[i:i+2] == 'z=':
        alphabet['z='] +=1
    else: 
        flag2 = True
    if flag2:
        i += 1
    elif flag:
        i += 3
    else:
        i += 2
answer = len(word)
for each in alphabet.items():
    if len(each[0]) == 2:
        answer -= each[1]
    else:
        answer -= 2*each[1]
print(answer)