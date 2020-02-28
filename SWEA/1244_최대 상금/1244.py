T = int(input())
for tc in range(1, T + 1):
    number, exchange = input().split()
    number = list(number)
    sorted_num = sorted(number, reverse=True)

    result = [number]
    flag = False
    for u in range(int(exchange)):
        lists = []
        if flag:
            temp = flag_num[-1]
            flag_num[-1] = flag_num[-2]
            flag_num[-2] = temp
            lists.append(flag_num)
        else:
            for m in result:
                counter = 0
                while True:
                    for i in range(counter + 1, len(m)):
                        temp = [a for a in m]
                        temporary = temp[counter]
                        temp[counter] = temp[i]
                        temp[i] = temporary
                        lists.append(temp)
                        if temp == sorted_num:
                            flag = True
                            flag_num = sorted_num
                            break
                    counter += 1
                    if counter == len(m)-1:
                        break
                    if flag:
                        break
                if flag:
                    break
        result = lists

    final = []
    for i in result:
        final.append(int(''.join(i)))
    print('#{} {}'.format(tc, max(final)))


