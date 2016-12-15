# coding: utf-8;

def search(i, j):
    global h, w, m

    if m[i][j] == 'g': return True
    if m[i][j] == '#': return False
    cl = list(m[i])
    cl[j] = '#'
    m[i] = "".join(cl)

    res = False
    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 > i + a or i + a >= h or 0 > j + b or j + b >= w: continue
        res = search(i + a, j + b)
        if res: break
    return res

def main():
    s = ()

    for i in range(h):
        c = input()
        m.append(c)

    if 's' in m[0]:
        s = (i, m[0].index('s'))

    if search(s[0], s[1]):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    h, w = map(int, input().split())
    m = []
    r = []
    main()
