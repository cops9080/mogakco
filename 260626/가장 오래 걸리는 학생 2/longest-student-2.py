import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j, d = map(int, input().split())
    graph[j].append((i, d)) # 간선 방향 뒤집기

def dijkstra(graph, school):
    queue = []
    dist = [INF] * (N+1)

    heapq.heappush(queue, (0, school))
    dist[school] = 0

    while queue:
        current_time, current_node = heapq.heappop(queue)

        if dist[current_node] < current_time:
            continue
        
        for friend, time in graph[current_node]:
            new_time = current_time + time

            if new_time < dist[friend]:
                dist[friend] = new_time
                heapq.heappush(queue, (new_time, friend))

    return dist

result = dijkstra(graph, N)
result.remove(INF)
ans = max(result)
print(ans)
