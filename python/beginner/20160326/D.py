# coding: utf-8;

def bellman_ford(graph, cost, t):
    start = 0
    cost[start] = 0

    for edge_from, from_nodes in enumerate(graph):
        for edge_to, edge_cost in enumerate(from_nodes):
            if cost[edge_from] != t and edge_cost > 0 and cost[edge_to] > cost[edge_from] + edge_cost:
                cost[edge_to] = cost[edge_from] + edge_cost
    return cost

def main():
    n, m, t = map(int, input().split())
    th =[int(i) for i in input().split()]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    reverse_graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a][b] = c
        reverse_graph[b][a] = c

    print(treasure_hant(n, m, t, th, graph, reverse_graph))    

def treasure_hant(n, m, t, th, graph, reverse_graph):
    cost = [t for _ in range(n)]
    reverse_cost = [t for _ in range(n)]

    cost = bellman_ford(graph, cost, t)
    reverse_cost = bellman_ford(reverse_graph, reverse_cost, t)

    max_money = 0

    for i in range(n):
        m = (t - cost[i] - reverse_cost[i]) * th[i]
        if m > max_money:
            max_money = m

    return max_money

if __name__ == '__main__':
    main()
