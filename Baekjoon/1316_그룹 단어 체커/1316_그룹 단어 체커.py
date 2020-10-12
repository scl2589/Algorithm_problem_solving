# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우를 말한다.
N = int(input())
count = 0
for _ in range(N):
    word = input()
    already = []
    flag = False
    prev = ''
    i = 0
    while i < len(word):
        if word[i] != prev:
            if word[i] not in already:
                already.append(word[i])
                prev = word[i]
            else:
                flag = True
                break
        i += 1
    if not flag:
        count += 1
print(count)