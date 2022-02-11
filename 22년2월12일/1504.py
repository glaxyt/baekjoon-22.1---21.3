# 1504번 특정한 최단 경로
# 다익스트라 + 완전탐색
import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    return distance

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
num1, num2 = map(int, input().split())

# 무조건 거쳐야 하는 정점이기에 
# 경로 2개가 있다. 1 - num1 - num2 - n 이랑 1 - num2 - num1 - n 
# 둘의 최단거리 비교 만일 도착점을 거치지 못했다면 둘의 최단경로 값은 INF를 한참 넘어서는 값이 될것이다.
first = dijkstra(1)
n_num1 = dijkstra(num1)
n_num2 = dijkstra(num2)

check = min(first[num1] + n_num1[num2] + n_num2[n], first[num2] + n_num2[num1] + n_num1[n])
if check < INF:
    print(check)
else:
    print(-1)
