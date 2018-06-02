def main():
    N = int(input())
    A = list(map(int, input().split()))
    x = 0
    s = 0
    r = 0
    res = 0
    for l in range(N):
        while N > r:
            if s & A[r] != 0: break
            s += A[r]
            r += 1

        s -= A[l]
        res += r - l

    print(res)
if __name__ == '__main__':
    main()