# coding: utf-8

def main():
    N = int(input())
    total_p = 0
    main_town = ('atcoder', 0)

    for n in range(N):
        s, p = input().split()
        p = int(p)
        total_p += p
        if 0 > total_p - p * 2:
            main_town = (s, p)
        elif total_p - main_town[1] * 2 >= 0:
            main_town = ('atcoder', 0)

    print(main_town[0])


if __name__ == '__main__':
    main()
