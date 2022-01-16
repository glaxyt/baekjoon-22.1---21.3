# 17086번 아기 상어 2
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, 1, -1, 1, -1, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append((nx, ny))

N, M = list(map(int, input().split()))
safe_dis = 0

graph = []
queue = deque()     # 덱 생성
for i in range(N):  # dfs에 쓸 배열 및, 아기상어 위치 찾아서 덱에 넣어주기
    args = list(map(int, input().split()))
    for k in range(M):
        if args[k] == 1:
            queue.append((k,i))     # 아기상어가 있는곳부터 덱에 넣어서 bfs 실행
    graph.append(args)
                    
bfs()

for h in range(N):  # 가장 큰 거리 값을 계산
    for d in range(M):
        safe_dis = max(safe_dis, graph[h][d])

print(safe_dis)
