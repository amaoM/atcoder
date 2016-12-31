# coding: utf-8;
# WIP

def main():
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    side_count = [0 for _ in range(m)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x - 1][y - 1] = 1
        side_count[y - 1] += 1

    for i, c in enumerate(side_count):
        if c != 0: continue
        for j, k in enumerate(graph[i]):
            if k == 0: continue
            side_count[j] -= 1

if __name__ == '__main__':
    main()
