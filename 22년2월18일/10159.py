# 10159번 저울
# 플로이드 와샬 알고리즘 사용
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
# 숫자가 들어가서 INF를 대체하면 아래서 숫자 비교가 가능하다는 뜻이다.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 노드 a와 비교가 가능한 노드의 개수 cnt
for a in range(1, n+1):
    cnt = 0
    for b in range(1, n+1):
        # 양쪽에서 비교가 불가능해야한다.
        if graph[a][b] == INF and graph[b][a] == INF:
            cnt += 1

    print(cnt)
