origin = int(input())
num = origin
count = 0
while True:
    num = num%10*10 + (num%10+num//10) % 10
    count += 1
    if num == origin:
        break
print(count)
