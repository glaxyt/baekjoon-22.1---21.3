# 2667번 단지번호붙이기
# 배열은 한변이 N인 정사각형, 시작점이 없기에 잡아줘야한다. 이동방향은 상하좌우
# 단지의 개수, 오름차순(줄바꿈)으로 출력되는 단지 내 집의 개수들 bfs사용
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    house = 1       # 집을 발견해서 덱에 넣어놨기에 1 추가
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0<= ny < N:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = '*'
                    queue.append((nx, ny))
                    house +=1
    return house


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
graph = []

for k in range(N):
    args = list(map(int, input().rstrip()))
    graph.append(args)

queue = deque()
cnt = 0         # 단지 개수
home_num = []   # 집의 개수를 저장할 리스트
for k in range(N):
    for j in range(N):
        if graph[k][j] == 1:
            graph[k][j] = '*'
            queue.append((j, k))
            home_num.append(bfs())
            cnt += 1            # 인접된 집을 모두 탐색했기에 1 추가

home_num = sorted(home_num)     # 단지 내 집의 개수 정렬

print(cnt)
for i in home_num:
    print(i)
