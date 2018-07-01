def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    m = min(A)
    mi = A.index(m)
    c = (N - 1) // (K - 1)
    if (N - 1) % (K - 1) > 0: c += 1
    print(c)

if __name__ == '__main__':
    main()