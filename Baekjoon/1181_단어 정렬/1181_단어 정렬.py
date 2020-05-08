num = int(input())
words = []
for _ in range(num):
    words.append(input())
new_word = sorted(set(words), key=lambda x: (len(x),x))
for i in new_word:
    print(i)