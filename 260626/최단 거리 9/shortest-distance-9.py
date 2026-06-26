import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

A, B = map(int, input().split())

def dijkstra(graph, start, end):
    queue = []
    dist = [INF] * (N+1)
    prev = [-1] * (N+1) # 이전 노드 추적

    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        if dist[current_node] < current_cost:
            continue

        for v, w in graph[current_node]:
            new_cost = dist[current_node] + w

            if new_cost < dist[v]:
                dist[v] = new_cost
                # v의 이전 노드가 current_node임을 기록
                prev[v] = current_node

                heapq.heappush(queue, (new_cost, v))

    path = []
    current = end

    while current != -1:
        path.append(current)
        current = prev[current]

    path.reverse()
    return dist[end], path

cost, result = dijkstra(graph, A, B)
print(cost)
print(*result, sep=' ')