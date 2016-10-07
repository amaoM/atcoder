# coding: utf-8

def main():
    w, h = map(int, input().split())
    mx = max(w-1, h-1)
    mn = min(w-1, h-1)

    mod = 1000000007
    d = 1
    m = 1

    for i in range(mx+1, mx+mn+1):
        m *= i

    for k in range(1, mn+1):
        d *= k

    print(m * pow(d, mod-2, mod) % mod)

if __name__ == '__main__':
    main()
