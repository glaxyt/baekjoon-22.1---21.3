# 1238번 파티
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    distance= [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for v, w in graph[now]:
            cost = w + dist
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    return distance

n, m, target = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 가장 큰값을 찾아주기 위한 세팅
maximum = 0
# 파티가 열리는 장소에서 각 마을로 가는데 걸리는 최단경로
dist_target = dijkstra(target)
# 마을 ->파티 경로랑 파티 -> 마을 경로를 더해서 max값을 잡아준다.
for i in range(1, n+1):
    dist_i = dijkstra(i)
    maximum = max(maximum, dist_i[target] + dist_target[i])

print(maximum)
