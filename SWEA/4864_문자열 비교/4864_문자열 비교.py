T = int(input())
for tc in range(1, T+1):
    str1= input()
    str2= input()
    if str1 in str2:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))