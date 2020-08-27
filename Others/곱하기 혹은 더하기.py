S= [int(i) for i in list(input())]
max = 0
first = S[0]
for i in range(1, len(S)):
    num = S[i]
    if num <= 1 or first <= 1:
        first += num
    else:
        first *= num 
print(first) 
