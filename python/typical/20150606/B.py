# coding: utf-8;

class UnionFind:
    root = []
    rank = []

    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, i):
        if self.root[i] == i:
            return i
        return self.find(self.root[i])

    def unite(self, i, j):
        ri = self.root[i]
        rj = self.root[j]
        if ri > rj:
            self.root[ri] = rj
        else:
            self.root[rj] = ri

    def same(self, i, j):
        return self.root[i] == self.root[j]

def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    res = []
    for _ in range(q):
        p, a, b = map(int, input().split())
        if p == 0:
            uf.unite(a, b)
        else:
            if uf.same(a, b):
                res.append('Yes')
            else:
                res.append('No')

    for r in res: print(r)

if __name__ == '__main__':
    main()
