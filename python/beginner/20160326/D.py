# coding: utf-8;

def main():
    n, m, t = map(int, input().split())
    th = list(map(int, input().split()))
    graph = [[0 for _ in range(3)] for _ in range(m)]
    reverse_graph = [[0 for _ in range(3)] for _ in range(m)]
    cost = [t for _ in range(n)]
    reverse_cost = [t for _ in range(n)]
    prev = [None for _ in range(n)]
    reverse_prev = [None for _ in range(n)]

    for i in range(m):
        a, b, c = map(int, input.split())
        grap[i][0] = a
        grap[i][1] = b
        grap[i][2] = c
        reverse_graph[i][0] = b
        reverse_graph[i][1] = a
        reverse_graph[i][2] = c

    start = 0
    cost[start] = 0

    for edge_from, from_nodes in enumerate(graph):
        for edge_to, edge_cost in enumerate(from_nodes):
            if cost[edge_to] != t and edge_cost > 0 and cost[edge_to] > cost[edge_from] + edge_cost:
                cost[edge_to] = cost[edge_from] + edge_cost

if __name__ == '__main__':
    main()
