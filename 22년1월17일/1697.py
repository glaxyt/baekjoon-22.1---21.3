# 1697번 숨바꼭질
# 시작값과 목표값도 주어짐 배열 한계는 0 - 100000 까지
# 이동방향은 3가지 [+1, -1, 이전값*2], 최적의 거리를 찾기에 bfs사용
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(N)
    graph[N] = 1
    while queue:
        x = queue.popleft()
        for k in [1, -1, x]:
            nx = x + k
            if 0 <= nx <= 100000:
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    queue.append(nx)

N, K = map(int, input().split())
graph = [0] * 100001    # 인덱스 0까지 포함하기에 자리는 100001개 있어야한다.
bfs()

print(graph[K]-1)       # 시작점에 1이 적혀있기에 1을 빼줘야한다.
