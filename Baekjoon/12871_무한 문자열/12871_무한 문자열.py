import math

s = input()
t = input()

lcm = len(s)*len(t)//math.gcd(len(s), len(t))
s = s * (lcm//len(s))
t = t * (lcm//len(t))

if s == t:
    print(1)
else:
    print(0)