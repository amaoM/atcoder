# coding: utf-8;

def main():
    r, c = map(int, input().split())
    sy, sx = map(lambda x:int(x) - 1, input().split())
    gy, gx = map(lambda x:int(x) - 1, input().split())
    m = []
    d = []
    n = 0
    reached = [[0 for _ in range(c)] for _ in range(r)]

    for _ in range(r): m.append(list(input()))

    queue = [(sx, sy, 0)]

    while len(queue) != 0:
        px, py, n = queue.pop(0)
        for nx, ny in [(px + 1, py), (px, py + 1), (px - 1, py), (px, py - 1)]:
            if reached[ny][nx] != 0 or \
                m[ny][nx] == '#' or \
                0 > nx or 0 > ny or nx + 1 > c or ny + 1 > r:
                continue
            if (nx, ny) == (gx, gy):
                d.append(n + 1)
                continue
            queue.append((nx, ny, n + 1))
            reached[ny][nx] = 1

    print(min(d))

if __name__ == '__main__':
    main()
