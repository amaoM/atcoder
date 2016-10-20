# coding: utf-8

def main():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x][y] = 1
        graph[y][x] = 1

    dijkstras(graph, a - 1, n, m)

def dijkstras(graph, start, goal, load_numbers):
    max_cost = 200
    cost = [max_cost for _ in range(goal)]
    prev = [[] for _ in range(goal)]
    visited = [False for _ in range(goal)]

    cost[start] = 0
    prev[start].append(start)
    node = start

    while True:
        min_cost = max_cost
        visited[node] = True
        next_node = -1

        for i in range(goal):
            if visited[i] == True: continue
            if graph[node][i]:
                d = cost[node] + graph[node][i]
                if cost[i] >= d:
                    cost[i] = d
                    prev[i].append(node)
            if min_cost > cost[i]:
                min_cost = cost[i]
                next_node = i
        node = next_node
        if next_node == -1: break

    for i in range(goal):
        print("{}, prev = {}, cost = {}".format(i, prev[i], cost[i]))

if __name__ == '__main__':
    main()
