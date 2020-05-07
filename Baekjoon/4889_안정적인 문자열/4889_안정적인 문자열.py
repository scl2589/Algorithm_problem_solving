tc = 0
while True:
    arr = input()
    tc += 1
    #여느 괄호의 갯수를 세는 variable
    count = 0
    answer = 0
    if arr[0] == '-':
        break
    else:
        for i in arr:
            #여는 괄호를 만났을 때
            if i == '{':
                count += 1
            #닫는 괄호를 만났을 때
            else:
                #만약 이전에 여는 괄호가 없었다면
                if count <= 0:
                    answer += 1
                    count += 1
                #만약 이전에 여는 괄호가 있었다면
                else:
                    count -= 1
        answer += count//2
        print('{}. {}'.format(tc, answer))