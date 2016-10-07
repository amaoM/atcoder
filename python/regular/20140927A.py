# coding: utf-8

if __name__ == '__main__':
    N = int(input())
    t_list = sorted([int(input()) for _ in range(N)], reverse=True)

    a = 0
    b = 0

    for t in t_list:
        if b > a:
            a += t
        else:
            b += t

    print(max(a, b))
