# coding: utf-8

def main():
    N = int(input())
    power = [1, 2, 4, 8]

    i = len(power) - 1
    res = []

    while i >= 0:
        if N >= power[i]:
            res.append(power[i])
            N -= power[i]
        else:
            i -= 1

        if N == 0: break

    print(len(res))
    for r in res:
        print(r)

if __name__ == '__main__':
    main()
