# 17396번 백도어
# 다익스트라 문제, 최대가 300억인 경우
import sys
import heapq
input = sys.stdin.readline
# INF 1000억
INF = int(1e11)

# 다익스트라 알고리즘 사용
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    distance[0] = 0
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

n, m = map(int, input().split())

# 시야가 보여서 가짐 못하는 분기점을 set에 넣어준다.
wad = list(map(int, input().split()))
wad_set = set()
for i in range(n-1):
    if wad[i] == 1:
        wad_set.add(i)

# 다익스트라 기본 세팅
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int,input().split())
    # 앞서 만든 가지 못하는 분기점에 해당하는 vertex가 나오면 간선을 만들지않는다.
    if a not in wad_set and b not in wad_set:
        graph[a].append((b, c))
        graph[b].append((a, c))

dijkstra()
ans = distance[n-1]

if ans == INF:
    print(-1)
else:
    print(ans)
