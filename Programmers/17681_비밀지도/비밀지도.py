def solution(n, arr1, arr2):
    answer = []
    arr1_bit = [bin(i) for i in arr1]
    arr2_bit = [bin(i) for i in arr2]

    arr1_new = []
    arr2_new = []
    
    for bit in arr1_bit:
        new = bit.split('b')[1]
        if len(new) != n:
            new = (n - len(new))*'0' + new
        arr1_new.append(new)
        
    for bit in arr2_bit:
        new = bit.split('b')[1]
        if len(new) != n:
            new = (n - len(new))*'0' + new
        arr2_new.append(new)
    # print(arr1_new, arr2_new)
    for i in range(n):
        temp =  ""
        for j in range(n):
            if arr1_new[i][j] == '1' or arr2_new[i][j]=='1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer

# 더 효율적, 빠른 코드
def solution(n, arr1, arr2):
    answer = []
    zipped = zip(arr1, arr2)
    for n1, n2 in zipped:
        temp = bin(n1 | n2)[2:]
        if len(temp) < n:
            temp = '0' * (n - len(temp)) + temp 
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)
    return answer