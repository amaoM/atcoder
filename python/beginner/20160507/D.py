# coding: utf-8;

def main():
    h, w = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    c = 0

    for y, r in enumerate(graph):
        for x, ta in enumerate(r):
            queue = [([ta], y, x)]
            c += 1
            while queue:
                q = queue.pop(0)
                prev = q[0]
                a = prev[-1]
                y = q[1]
                x = q[2]

                if h > y + 1 and graph[y + 1][x] > a:
                    queue.append((prev + [graph[y + 1][x]], y + 1, x))
                    c += 1
                if w > x + 1 and graph[y][x + 1] > a:
                    queue.append((prev + [graph[y][x + 1]], y, x + 1))
                    c += 1
                if y > 0 and graph[y - 1][x] > a:
                    queue.append((prev + [graph[y - 1][x]], y - 1, x))
                    c += 1
                if x > 0 and graph[y][x - 1] > a:
                    queue.append((prev + [graph[y][x - 1]], y, x - 1))
                    c += 1
                print(prev)
    print(c)

if __name__ == '__main__':
    main()
