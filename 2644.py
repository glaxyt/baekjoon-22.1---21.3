# 2644번 촌수 계산
# 가까운 곳부터 계산하는 bfs사용
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1     # 이전에 거쳐온 visited에 거리값을 적어놨기 때문에 +1만해주면 start에서부터 얼마나 걸리는지 알 수 있다.

n = int(input())
m1, m2 = list(map(int, input().split()))
graph = [[]for _ in range(n+1)]
visited = [-1] * (n+1)
for i in range(int(input())):
    arg1, arg2 = list(map(int, input().split()))
    graph[arg1].append(arg2)
    graph[arg2].append(arg1)

bfs(m1)
print(visited[m2])
