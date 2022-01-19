# 7569번 토마토
# 이동방향 상하좌우 + 상자 위아래
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    pass

dx = [0, 0, 1, -1]      # 토마토 익는 이동방향
dy = [1, -1, 0, 0]
dz = [0, 1, -1]

# N = 가로, M = 세로, H = 상자 개수
N, M, H = map(int, input().split())

# 토마토를 쌓아놓을 상자
tomatoes = [[] for _ in range(H)]

# 토마토 인풋 대입
queue = deque()
i = 0
for y in range(M):
        args = list(map(int, input().split()))
        tomatoes[i].append(args)
        for x in args:
            if x == 1:
                queue.append((x, y, i))
        i += 1
# 모든 토마토가 익었다고 보여주는 코드.
# 토마토가 모두 익지 못하면 -1
# 시작부터 전부 익어있으면 0
# 모든 토마토가 익는데 걸리는 최소일수 보여주기