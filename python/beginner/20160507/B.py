# coding: utf-8;

def main():
    n, q = map(int, input().split())
    nl = [0 for _ in range(n)]

    for _ in range(q):
        l, r, t = map(int, input().split())
        for i in range(l, r + 1):
            nl[i - 1] = t

    for i in nl: print(i)

if __name__ == '__main__':
    main()
