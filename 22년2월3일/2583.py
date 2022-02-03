# 2583번 영역 구하기
# 중복된 값은 어떻게 빼줄것인가, 삼중 for문은 비효율, 마지막에 어떻게 개수를 세줄것인가.
# 나누어진 영역 값을 어떻게 빼줄것인가. bfs 사용 
import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())

# 리스트로 직사각형 생성
rect = [[0]*N for i in range(M)]

# 이동방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # 범위 설정은 항상 x1이 x2보다 작고 y1이 y2보다 작다고 주어졌기에 가능(직사각형의 좌표는 자연수의 범위에 있다)
    for i in range(x1, x2):
        for j in range(y1, y2):
            rect[j][i] = 1

def bfs():
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= (N-1) and 0 <= ny <= (M-1) and rect[ny][nx] == 0:
                cnt += 1
                rect[ny][nx] = 1
                queue.append((nx, ny))
    return cnt

area = 0
arr = []
for y in range(M):
    for x in range(N):
        if rect[y][x] == 0:
            rect[y][x] = 1
            queue.append((x, y))
            arr.append(bfs())
            area += 1

arr.sort()
print(area)
for i in arr:
    print(i, end=' ')
