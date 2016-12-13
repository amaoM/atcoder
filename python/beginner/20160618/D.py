# coding: utf-8;

def dp(g, a, w, ps):
    for b, y in g[a]:
        if y == 0: continue
        if (a, b) in ps or (b, a) in ps: continue
        if w >= y: continue
        ps.append((a, b))
        dp(g, b, w, ps)
    return ps

def main():
    n, m = map(int, input().split())
    g = [[[0, 0] for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        a, b, y = map(int, input().split())
        g[a - 1].append([b - 1, y])
        g[b - 1].append([a - 1, y])

    q = int(input())
    res = [[] for _ in range(q)]

    for i in range(q):
        v, w = map(int, input().split())
        res[i] = [v - 1]
        ps = dp(g, v - 1, w, [])

        for p in ps:
            res[i] += list(p)

    for i in range(q):
        print(len(set(res[i])))

if __name__ == '__main__':
    main()
