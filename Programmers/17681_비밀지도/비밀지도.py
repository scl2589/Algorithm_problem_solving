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

# 이전에 풀었던 코드
def solution(n, arr1, arr2):
    arr = [[0]* n for _ in range(n)]
    list1 = []
    list2 = []
    for i in range(n):
        remain1 = ""
        remain2 = ""
        num1 = arr1[i]
        num2 = arr2[i]
        # 이진수 구하기
        for _ in range(n):
            remain1 = str(num1 % 2) + remain1
            num1 //= 2
        # string을 리스트로 만들기
        list1.append(list(map(int, list(remain1))))
        # 이진수 구하기
        for _ in range(n):
            remain2 = str(num2 % 2) + remain2
            num2 //= 2
        # string을 리스트로 만들기
        list2.append(list(map(int, list(remain2))))
        
    # 이진수 돌면서 벽 표시하기 
    for i in range(n):
        for j in range(n):
            if list1[i][j] == 1 or list2[i][j]==1:
                arr[i][j] = 1
                
    # 정답 배열 만들기
    answer = []
    for i in range(n):
        string = ""
        for j in arr[i]: 
            if j == 1:
                string += "#"
            else:
                string += " "
        answer.append(string)
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