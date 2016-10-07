# coding: utf-8

if __name__ == '__main__':
    A, B = map(int, input().split())
    if B > A:
        A, B = B, A
    N = int(input())
    res = []
    checked_list = {}

    for _ in range(N):
        C, D = map(float, input().split())

        if D > C:
            C, D = D, C

        if C >= A and D >= B:
            res.append('YES')
            continue

        if (C ** 2 + D ** 2) ** 0.5 >= (A ** 2 + B ** 2) ** 0.5:
            res.append('YES')
            continue

        res.append('NO')

    for r in res:
        print(r)
