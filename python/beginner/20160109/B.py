# coding: utf-8

s = input()
k = int(input())
passwords = []

if k > len(s):
    print(0)
else:
    for i in range(0, len(s) - k + 1):
        password = s[i:i+k]
        if password not in passwords:
            passwords.append(password)
    print(len(passwords))
