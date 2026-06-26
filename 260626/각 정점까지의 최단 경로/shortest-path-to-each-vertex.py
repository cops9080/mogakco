import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

N, M = map(int, input().split())
K = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(graph, start):
    queue = []
    dist = [INF] * (N+1)

    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        # 가장 작은 비용과 그 때의 정점을 큐에서 꺼낸다
        current_cost, current_node = heapq.heappop(queue)

        if dist[current_node] < current_cost:
            continue
        
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
    
    return dist

result = dijkstra(graph, K)
for i in range(1, N+1):
    if result[i] == INF:
        print(-1)
    else:
        print(result[i])