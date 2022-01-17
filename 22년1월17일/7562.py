# 7562번 나이트의 이동
# 배열의 크기는 가로, 세로가 I. 시작점, 목표점이 주어짐, 이동방향은 나이트의 이동 8개
# bfs는 최적의 수를 주기에 visited 안에서 이동할때마다 1씩 추가해준다.
import sys
from collections import deque
input = sys.stdin.readline


dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        start_x, start_y = queue.popleft()
        if start_x == end_x and start_y == end_y:
            print(visited[start_x][start_y] - 1)        # 목표값 도착(시작점이 1이기에 1을 빼준다.)
            return True

        for i in range(8):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:  # 반대되는 조건을 붙일시에는 continue로 사용할 수 있다.
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[start_x][start_y] + 1
                queue.append((nx, ny))
    return False
        
N = int(input())

for i in range(N):
    I = int(input())
    visited = [[0]*I for i in range(I)]
    X1, Y1 = list(map(int, input().split()))
    X2, Y2 = list(map(int, input().split()))
    visited[X1][Y1] = 1                 # 시작점이 주어졌기에 방문처리
    bfs(X1, Y1, X2, Y2)
