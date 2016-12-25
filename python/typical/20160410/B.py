# coding: utf-8;

def main():
    n, m, p = map(int, input().split())

    def pow_mod(n, m, p):
        if p == 0: return 1
        if p % 2 == 0:
            i = pow_mod(n, m, p / 2)
            return i * i % m
        return pow_mod(n, m, p - 1) * n % m

    print(pow_mod(n, m, p))


if __name__ == '__main__':
    main()
