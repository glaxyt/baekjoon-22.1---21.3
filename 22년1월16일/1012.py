# 1012번 유기농 배추
# 인접한 부분을 하나의 독립된 개체로 본다.(인접기준은 상하좌우)
# 2차원 배열이기에 좌표가 필요하다.(M = 가로길이, N = 세로길이)
# 타겟은 주어졌다. (배추는 K개)
# bfs 사용할것이다.
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 2
                    queue.append((nx, ny))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)] # 2차원 배열 완성
    total =0
    queue = deque()

    for _ in range(K):      # 배추 위치를 2차원 배열에 추가(배추의 위치는 1)
        x, y = map(int, input().split())
        graph[y][x] = 1

    for arg_y in range(N):  # 배추밭에 배추를 찾아서 2로 바꿔준 뒤 덱에 넣어준다. 찾은 배추의 위치를 bfs함수에 넣어 인접된 배추의 위치 또한 2로 바꿔준다.
        for arg_x in range(M):
            if graph[arg_y][arg_x] == 1:
                graph[arg_y][arg_x] = 2
                queue.append((arg_x, arg_y))
                bfs()
                total += 1      # bfs로 인접된 배추를 남김없이 찾았으면 total에 1추가
    print(total)