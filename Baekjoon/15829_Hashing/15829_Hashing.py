L = int(input())
letters = input()
total = 0
for i in range(L):
    total += (ord(letters[i])-96)*(31**i)
print(total % 1234567891)