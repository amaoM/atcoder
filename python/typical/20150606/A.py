# coding: utf-8;

def main():
    s = ()

    for i in range(h):
        c = list(input())
        m.append(c)

        if 's' in c: s = (i, c.index('s'))

    stack = [s]
    res = False

    while len(stack) != 0:
        i, j = stack.pop()

        if m[i][j] == 'g':
            res = True
            break

        if m[i][j] == '#': continue

        m[i][j] = '#'

        for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 > i + a or i + a >= h or 0 > j + b or j + b >= w: continue
            stack.append((i + a, j + b))

    if res:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    h, w = map(int, input().split())
    m = []
    r = []
    main()
