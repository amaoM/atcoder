# coding: utf-8;

def main():
    n, k = map(int, input().split())
    a = input().split()

    pa = [int(i) for i in a[:n - k + 1]]
    res = sum(pa)

    for b in a[n - k + 1:]:
        pa.pop(0)
        pa.append(int(b))
        res += sum(pa)

    print(res)

if __name__ == '__main__':
    main()
