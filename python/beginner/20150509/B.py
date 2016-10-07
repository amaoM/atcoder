# conding: utf-8

def judge(N, S):
    n = (N - 1) / 2

    if n != int(n):
        return -1

    n = int(n)

    for l in range(n):
        left = S[n - l - 1]
        right = S[n + l + 1]
        if l % 3 == 0 and left == 'a' and right == 'c':
            continue
        if l % 3 == 1 and left == 'c' and right == 'a':
            continue
        if l % 3 == 2 and left == 'b' and right == 'b':
            continue
        return -1

    return n

if __name__ == '__main__':
    N = input()
    S = input()

    result = judge(int(N), S)
    print(result)