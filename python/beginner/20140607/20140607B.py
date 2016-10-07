# coding: utf-8

if __name__ == '__main__':
    # n = int(input())
    # a_list = input().split()
    # petal = 0
    #
    # for i in range(n):
    #     a = int(a_list[i])
    #     if a == 1: continue
    #
    #     while True:
    #         if a % 2 == 0 or a % 3 == 2:
    #             petal += 1
    #             a -= 1
    #         else:
    #             break
    #
    # print(petal)

    n = int(input())
    a_list = map(int, input().split())
    petal_list = [3, 0, 1, 0, 1, 2]
    petal = 0

    for a in a_list:
        petal += petal_list[a % 6]

    print(petal)
