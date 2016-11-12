import heapq

def dijkstras(clist):
    INT_MAX = 10 ** 9
    distance = [INT_MAX] * len(clist)
    distance[0] = 0
    queue = [(0, 0)]

    while queue:
        di, i = heapq.heappop(queue)
        if distance[i] < di:
            continue
        for j, dj in clist[i]:
            if dj + distance[i] < distance[j]:
                distance[j] = distance[i] + dj
                heapq.heappush(queue, (distance[j], j))

    return distance


if __name__ == '__main__':
    n, m, t = [int(i) for i in input().split(' ')]
    income = [int(i) for i in input().split(' ')]
    edges_fwd = [[] for _ in range(n)]
    edges_rev = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = [int(i) for i in input().split(' ')]
        edges_fwd[a - 1].append((b - 1, c))
        edges_rev[b - 1].append((a - 1, c))

    edges_fwd = tuple(tuple(edge) for edge in edges_fwd)
    edges_rev = tuple(tuple(edge) for edge in edges_rev)
    distance_fwd = dijkstras(edges_fwd)
    distance_rev = dijkstras(edges_rev)

    money = [ic * (t - df - dr) for ic, df, dr in zip(income, distance_fwd, distance_rev)]
    print(max(money))
