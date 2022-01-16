# 2178 미로찾기
# BFS로 찾을예정 BFS는 최적의 수를 주기에, 상하좌우만 가능. 1.1 - N.M 까지 가는데에 최단경로
# N(세로), M(가로) 순으로 입력 그 이후는 배열입력
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    graph[0][0] = 1
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == '1':
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = []

for i in range(N):      # 배열 완성
    args = list(input().rstrip())
    graph.append(args)

bfs()

print(graph[N-1][M-1])
