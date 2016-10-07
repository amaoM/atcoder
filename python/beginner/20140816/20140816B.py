# coding: utf-8

if __name__ == '__main__':

    a = int(input())
    b = int(input())

    if abs(a - b) >= 5:
        print(10 - max(a, b) + min(a, b))

    else:
        print(abs(a - b))