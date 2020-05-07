word = input().lower()
letters = dict()
for i in word:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1
new_dict = sorted(letters.items(), key=lambda x: x[1], reverse= True)
if len(new_dict) > 1:
    if new_dict[0][1] == new_dict[1][1]:
        print('?')
    else:
        print(new_dict[0][0].upper())
else:
    print(new_dict[0][0].upper())