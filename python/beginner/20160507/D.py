# coding: utf-8;

import heapq

def main():
    h, w = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    c = 0
    pc = 0

    for sy in range(h):
        for sx in range(w):
            ta = graph[sy][sx]

            if visited[sy][sx] > 0:
                c += visited[sy][sx] - 1
                continue

            queue = [(ta, sy, sx)]
            c += 1

            while queue:
                q = heapq.heappop(queue)
                a = q[0]
                y = q[1]
                x = q[2]

                if h > y + 1 and graph[y + 1][x] > a:
                    heapq.heappush(queue, (graph[y + 1][x], y + 1, x))
                    c += 1
                if w > x + 1 and graph[y][x + 1] > a:
                    heapq.heappush(queue, (graph[y][x + 1], y, x + 1))
                    c += 1
                if y > 0 and graph[y - 1][x] > a:
                    heapq.heappush(queue, (graph[y - 1][x], y - 1, x))
                    c += 1
                if x > 0 and graph[y][x - 1] > a:
                    heapq.heappush(queue, (graph[y][x - 1], y, x - 1))
                    c += 1

            visited[sy][sx] = c - pc
            pc = c

    print(c % 1000000007)

if __name__ == '__main__':
    main()
