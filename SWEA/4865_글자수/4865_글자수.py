T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    dic1 = {}
    for i in str1:
        dic1[i]=0
    for i in str2:
        if i in dic1:
            dic1[i] += 1

    value = dic1.values()
    print('#{} {}'.format(tc, max(value)))
