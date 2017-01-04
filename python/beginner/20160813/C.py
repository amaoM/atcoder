# coding: utf-8;

def main():
    n = int(input())
    al = list(map(int, input().split()))
    mc = 10 ** 20

    for i in range(-100, 101):
        c = 0
        for a in al:
            c += (a - i) ** 2
        if mc > c: mc = c

    print(mc)

if __name__ == '__main__':
    main()
