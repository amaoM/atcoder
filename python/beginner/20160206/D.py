# coding: utf-8
import math

def main():
    N = int(input())
    point_list = []

    for n in range(N):
        x, y = map(int, input().split())
        point_list.append((x, y))

    for i, base_point in enumerate(point_list):
        other_point_list = point_list[:]
        del other_point_list[i]

        k = 0
        while len(other_point_list) > k:
            other_point_a = other_point_list[k]
            if k + 1 >= len(other_point_list):
                other_point_b = other_point_list[0]
            else:
                other_point_b = other_point_list[k + 1]
            (ax, ay) = (other_point_a[0] - base_point[0], other_point_a[1] - base_point[1])
            (bx, by) = (other_point_b[0] - base_point[0], other_point_b[1] - base_point[1])
            k += 1
            try:
                angle = math.acos((ax * bx + ay * by) / (math.sqrt((ax ** 2 + ay ** 2) * (bx ** 2 + by ** 2))))
                print('({}, {}), ({}, {}), ({}, {}) = {}'.format(base_point[0], base_point[1], other_point_a[0], other_point_a[1], other_point_b[0], other_point_b[1], math.degrees(angle)))
            except Exception as e:
                print('({}, {}), ({}, {}), ({}, {}) = zero'.format(base_point[0], base_point[1], other_point_a[0], other_point_a[1], other_point_b[0], other_point_b[1]))

        print('---')



if __name__ == '__main__':
    main()
