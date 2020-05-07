#각각의 알파벳에 대해서, 단어가 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력
word = input()
letters = [-1]*26
#97 ~ 122
for idx, value in enumerate(word):
    if letters[ord(value) - ord('a')] == -1:
        letters[ord(value) - ord('a')] = idx
for i in letters:
    print(i, end=' ')