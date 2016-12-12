# coding: utf-8;

def dp(n, g, a, w, ps, c):

    for b in range(n):
        if g[a][b] == 0: continue
        if (a, b) in ps or (b, a) in ps: continue
        if g[a][b] > w:
            ps.append((a, b))
            ps.append((b, a))
            dp(n, g, b, w, ps, c)
    return ps

def main():
    n, m = map(int, input().split())
    g = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        a, b, y = map(int, input().split())
        g[a - 1][b - 1] = y
        g[b - 1][a - 1] = y

    q = int(input())
    res = [[] for _ in range(q)]

    for i in range(q):
        v, w = map(int, input().split())
        res[i] = [v - 1]
        ps = dp(n, g, v - 1, w, [], 1)

        for p in ps:
            res[i] += list(p)

    for i in range(q):
        print(len(set(res[i])))

if __name__ == '__main__':
    main()
