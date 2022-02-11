# 5972번 택배 배송
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(target):
    q = []
    heapq.heappush(q, (0, 1))
    distance[0] = 0
    while q:
        dist, farm = heapq.heappop(q)
        # 애초에 지나온 경로의 값이 이전 도착값보다 크다면 패스
        if distance[farm] < dist:
            continue
        for v, w in graph[farm]:
            cost = dist + w
            if distance[v] > cost:
                distance[v]  = cost
                heapq.heappush(q, (cost, v))
    print(distance[target])

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(n)