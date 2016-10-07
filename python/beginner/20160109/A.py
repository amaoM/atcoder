# coding: utf-8

a = int(input())
b = int(input())
n = int(input())

x = min(a, b)
y = max(a, b)

while y > 0:
    x, y = y, x % y
gcd = x

lcm = a * b // gcd

if n % lcm != 0:
    print(lcm * ((n // lcm) + 1))
else:
    print(lcm * n // lcm)
