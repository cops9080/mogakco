import heapq
INF = int(10e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# Please write your code here.
def dijkstra(graph, start):
    queue = []
    dist = [INF] * (n+1)

    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if dist[current_node] < current_cost:
            continue
        
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))

    return dist


result = dijkstra(graph, 1)

for i in range(2, n+1):
    if result[i] == INF:
        print(-1)
    else:
        print(result[i])
    