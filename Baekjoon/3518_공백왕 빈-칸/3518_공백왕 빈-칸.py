# 풀지 못한 문제
# 입력값을 어떻게 받을 수 있을지 몰라 풀지 못했다.
import sys
sentences = sys.stdin.readline().split()
sentences = []
max_len = [0]*180
while True:
    try: 
        sentence = list(input().split())
        sentences.append(sentence)
        for i in range(len(sentence)):
            if max_len[i] < len(sentence[i]):
                max_len[i] = len(sentence[i])
    except:
        break
for i in range(len(sentences)):
    print(sentence[i].ljust(max_len[i]), end=" ")