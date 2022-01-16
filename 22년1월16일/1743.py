# 1743번 음식물 피하기
# bfs로 탐색 덱에 추가될때마다 1추가
# 이동방향은 상하좌우, 좌표가 (1,1)부터 시작이라 주의
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    cnt = 1     # bfs를 시작한 쓰레기 본인
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 2
                    queue.append((nx,ny))
                    cnt += 1        # 인접한 쓰레기를 발견할 때마다 1증가
            
    return cnt

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M, K = map(int, input().split())
graph = [[0]*(M) for _ in range(N)]

for i in range(K):       # 음식물 쓰레기 위치를 0에서 1로 바꿔준다.
    y, x = map(int, input().split())
    graph[y-1][x-1] = 1

queue = deque()
largest = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:    # 쓰레기를 발견한뒤 인접한 쓰레기를 확인했으면 2로 바꿔준다.
            graph[y][x] = 2
            queue.append((x, y))
            largest = max(largest, bfs())

print(largest)
