# 1916번 최소비용 구하기
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


city = int(input())
bus = int(input())
distance = [INF] * (city+1)
graph = [[] for i in range(city+1)]
for i in range(bus):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s, t = map(int, input().split())
dijkstra(s, t)
