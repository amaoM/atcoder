# coding: utf-8

def jump(point, D):
    yield (point[0] - D, point[1])
    yield (point[0] + D, point[1])
    yield (point[0], point[1] - D)
    yield (point[0], point[1] + D)

# def main(N, D, X, Y):
#     point = (0, 0)
#     point_list = [point]
#
#     for n in range(N):
#         next_point_list = []
#
#         for point in point_list:
#
#             for p in jump(point, D):
#                 next_point_list.append(p)
#
#         point_list = next_point_list
#
#
#     goal_count = 0
#
#     for point in point_list:
#
#         if point == (X, Y):
#             goal_count += 1
#
#     return round(goal_count / len(point_list), 9)


# def main(N, D, X, Y):
#     d = 1
#     x = X // D
#     y = Y // D
#     point = (0, 0)
#     point_list = [point]
#     goal_count = 0
#
#     for n in range(N):
#         next_point_list = []
#
#         for point in point_list:
#
#             if abs(point[0] - x) + abs(point[1] - y) > abs(N - n):
#                 continue
#
#             for p in jump(point, d):
#                 next_point_list.append(p)
#
#         point_list = next_point_list
#
#     return round((len(point_list) / 4) / (4 ** N), 9)


import itertools

def move(n, r_left):
    lfs = 1
    rhs = 1

    for l in range(n, 1, -1):
        lfs *= l

    for r in range(r_left - 1, 1, -1):
        rhs *= r

    return lfs / rhs

def main(N, D, X, Y):
    d = 1
    x = X // D
    y = Y // D
    res = 0

    for n in range(x, N):
        if (N - n) % 2 != y % 2:
            continue

        r_h = (n + x) // 2
        r_v = (N - n + y) // 2

        if n >= r_h and N - n >= r_v:
            print("h({}): {}, v({}): {}".format(n, r_h, N - n, r_v))
            res += move(n, r_h) * move(N - n, r_v) * move(N - n - x, n - r_h)

    print(res / (4 ** N))


if __name__ == '__main__':

    N, D = map(int, input().split())
    X, Y = map(int, input().split())
    main(N, D, X, Y)
