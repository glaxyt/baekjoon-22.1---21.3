# 14284번 간선 이어가기 2
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, target):
    q = []
    # heapq.heappush(dist, node)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # vertex, weight
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    print(distance[target])


n, m = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s, t = map(int, input().split())
dijkstra(s, t)
