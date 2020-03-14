T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    cnt - [0] * 128 #문자를 배열의 인덱스로 사용한다.
    
    for ch in str2:
        cht[ord(ch)] += 1
    ans = 0
    for ch in str 1:
        if cnt[ord(ch)]:
            ans = max(ans, cnt[ord(ch)])
            
    print("#%d %d" % (test_case, max(dict.values()))) 