# coding: utf-8;

def main():
    n = int(input())
    m = n

    for i in range(1, n + 1):
        j = int(n / i)
        d = abs(i - j) + n - i * j
        if m > d: m = d

    print(m)

if __name__ == '__main__':
    main()
