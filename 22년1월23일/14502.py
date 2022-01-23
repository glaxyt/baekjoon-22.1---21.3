# 14502번 연구소
# 벽 3개를 세워서 바이러스가 최대로 안퍼지게하고 안전영역의 최댓값을 구하기
# 바이러스는 상하좌우로 퍼진다. N = 세로, M = 가로
import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_result = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

def bfs():
    queue = deque()
    global max_result
    test = copy.deepcopy(graph)
    for y in range(N):
        for x in range(M):
            if test[y][x] == 2:
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if test[ny][nx] == 0:
                    test[ny][nx] = 2
                    queue.append((nx, ny))
    result = 0
    for y in range(N):
        for x in range(M):
            if test[y][x] == 0:
                result += 1
    max_result = max(max_result, result) 

def wall(cnt):      # 벽을 완전탐색으로 골라내는 함수
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt+1)
                graph[i][j] = 0

wall(0)
print(max_result)
