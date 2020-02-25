T = int(input())
for tc in range(1, T+1):
    nums = list(input())
    needed_people = 0
    for idx, value in enumerate(nums):
        #기립 박수를 하고 있는 사람이 아무도 없을 때, 기립 박수 하는 사람
        if idx == 0:
            if int(value) == 0:
                needed_people += 1
                clap = 1
            else:
                clap = int(value)
        #i번째~
        else:
            if int(value) >= 1:
                if clap >= idx:
                    clap += int(value)
                else:
                    more_people = idx - clap
                    needed_people += more_people
                    clap += more_people + int(value)
    print('#{} {}'.format(tc, needed_people))

