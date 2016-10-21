# coding: utf-8

def main():
    n = int(input())
    start, goal = map(lambda x: int(x) - 1, input().split())
    m = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x][y] = 1
        graph[y][x] = 1

    dijkstras(graph, start, goal, n)

def dijkstras(graph, start, goal, n):
    max_cost = 200
    cost = [max_cost for _ in range(n)]
    path_count = [0 for _ in range(n)]
    visited = [False for _ in range(n)]

    cost[start] = 0
    path_count[start] = 1
    node = start

    while True:
        min_cost = max_cost
        visited[node] = True
        next_node = -1

        for i in range(n):
            if visited[i] == True: continue
            if graph[node][i]:
                d = cost[node] + graph[node][i]
                if cost[i] >= d:
                    cost[i] = d
                    path_count[i] += path_count[node]
            if min_cost > cost[i]:
                min_cost = cost[i]
                next_node = i
        node = next_node
        if next_node == -1: break

    print(path_count[goal] % 1000000007)

if __name__ == '__main__':
    main()
