'''
처음에는 그저 palindrome만 생각하고 word == word[::-1]을 했으나,
'?'의 존재를 잊고 있었다.
예를 들어,
a?ba일 때 팰린드롬이 가능하다고 해야 하는데, 
위와 같은 방식에서는 ?와 b를 다르다고 인식하기에 팰린드롬이 불가능하다고 처리가 된다.
그렇게 때문에 이 부분을 주의해서 처리해야 한다.
'''
T = int(input())
for tc in range(1, T+1):
    word = list(input())
    flag = True
    while word:
        a = word.pop(0)
        b = word.pop()
        if a =='?' or b=='?':
            continue
        if a != b:
            flag = False
    if flag:
        print('#{} Exist'.format(tc))
    else:
        print('#{} Not exist'.format(tc))