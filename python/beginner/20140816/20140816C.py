# coding: utf-8

if __name__ == '__main__':
    total_price_list = []

    N, H = map(int, input().split())
    A, B, C, D, E = map(int, input().split())

    for X in range(N):
        Y = max(((N - X) * E - B * X - H) // (D + E) + 1, 0)
        total_price_list.append(X * A + Y * C)

    print(min(total_price_list))

