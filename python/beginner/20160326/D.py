# coding: utf-8;

def main():
    n, m, t = map(int, input().split())
    th = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    reverse_graph = [[0 for _ in range(n)] for _ in range(n)]
    cost = [t for _ in range(n)]
    reverse_cost = [t for _ in range(n)]
    prev = [None for _ in range(n)]
    reverse_prev = [None for _ in range(n)]

    for i in range(n):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a][b] = c
        reverse_graph[b][a] = c

    def bellman_ford(graph, cost, prev):
        start = 0
        cost[start] = 0

        for edge_from, from_nodes in enumerate(graph):
            for edge_to, edge_cost in enumerate(from_nodes):
                if cost[edge_from] != t and edge_cost > 0 and cost[edge_to] > cost[edge_from] + edge_cost:
                    cost[edge_to] = cost[edge_from] + edge_cost
                    prev[edge_to] = edge_from
        return cost, prev

    cost, prev = bellman_ford(graph, cost, prev)
    reverse_cost, reverse_prev = bellman_ford(reverse_graph, reverse_cost, reverse_prev)

    print(cost)
    print(prev)
    print(reverse_cost)
    print(reverse_prev)

if __name__ == '__main__':
    main()
