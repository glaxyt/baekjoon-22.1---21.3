# 1303 전쟁 - 전투
# 가로 N, 세로 M bfs에 넣을 위치 직접 찾아야함 방향은 상하좌우
# 아군, 적군 순으로 출력. B는 파랑(적군), W는 하양(아군) 뭉쳐있을경우 힘이 N^2로 올라간다.
import sys
from collections import deque
input = sys.stdin.readline

def bfs(color):
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if battlefield[ny][nx] == color:
                    battlefield[ny][nx] = 'X'
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
battlefield = []

for i in range(M):
    soldiers = list(input().rstrip())
    battlefield.append(soldiers)

white = 0
blue = 0

queue = deque()
for k in range(M):
    for j in range(N):
        if battlefield[k][j] == 'W':
            battlefield[k][j] = 'X'
            queue.append((j, k))
            white += (bfs('W') ** 2)

        elif battlefield[k][j] == 'B':
            battlefield[k][j] = 'X'
            queue.append((j, k))
            blue += (bfs('B') ** 2)

print(white, blue)
