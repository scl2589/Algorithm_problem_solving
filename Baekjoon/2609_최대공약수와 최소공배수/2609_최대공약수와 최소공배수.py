a, b = map(int,input().split())
gcd1 = 0
gcd2 = 0
#최대공약수 구하기
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i


#최소 공배수 = a//G * b//G * G
lcd = a//gcd * b//gcd * gcd

print(gcd)
print(lcd)