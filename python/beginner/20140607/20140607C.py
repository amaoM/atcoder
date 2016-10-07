# coding: utf-8
import math

if __name__ == '__main__':
    txa, tya, txb, tyb, T, V = map(int, input().split())
    n = int(input())
    girls = []
    result = 'NO'

    for i in range(n):
        x, y = map(int, input().split())

        if T * V >= math.sqrt((x - txa) ** 2 + (y - tya) ** 2) + math.sqrt((txb - x) ** 2 + (tyb - y) ** 2):
            result = 'YES'

    print(result)
