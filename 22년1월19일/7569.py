# 7569번 토마토
# 이동방향 상하좌우 + 상자 위아래
import sys
from collections import deque
input = sys.stdin.readline
# N = 가로, M = 세로, H = 상자 개수
N, M, H = map(int, input().split())
# 토마토
tomatoes = []
# 토마토 인풋 대입
queue = deque()

for z in range(H):
    tomato = []
    for y in range(M):
        args = list(map(int, input().split()))
        tomato.append(args)
        for x in range(N):
            if args[x] == 1:
                queue.append((x, y, z))
    tomatoes.append(tomato)

# 토마토 익는 이동방향
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                queue.append((nx, ny, nz))

bfs()

days = 0
for z in range(H):
    for y in range(M):
        for x in range(N):
            if tomatoes[z][y][x] == 0:
                print(-1)
                exit(0)
        days = max(days, tomatoes[z][y][x])
print(days-1)   # 시작값이 1이기에 1을 빼줘야한다.
