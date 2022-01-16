# 2438번 안전영역
# 크기가 N인 정사각형, 시작지점 없음 직접 찾아야함 최소 높이와 최대 높이 구하기
# 배열은 graph, visited로 구분
import sys
from collections import deque
input = sys.stdin.readline

def bfs(height, k, j):
    queue = deque()
    queue.append((k,j))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] == 0 and graph[ny][nx] > height:  # 방문하지않았으면서 비가내려도 안전지대인 곳
                    visited[ny][nx] = 1
                    queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
graph = []
maximum = 0                         # 높이 범위는 1-100 이기에
for _ in range(N):                  # 배열 작성 및 가장 큰 높이 구하기
    args = list(map(int, input().split()))
    graph.append(args)
    for j in range(N):
        maximum = max(maximum, args[j])

safe = []
for i in range(maximum+1):  # 비는 0에서 건물높이 최대치까지 내릴 수 있다. 
    visited=[[0]*N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:  # 방문하지않았으면서 비가내려도 안전지대인 곳
                visited[j][k] = 1
                bfs(i, k, j)
                cnt += 1
    safe.append(cnt)
print(max(safe))
