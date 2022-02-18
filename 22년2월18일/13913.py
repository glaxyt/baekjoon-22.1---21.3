# 13913 숨바꼭질
from collections import deque

def bfs():
    queue = deque()
    queue.append(s)
    distance[s] = 1
    while queue:
        x = queue.popleft()
        # 목표값에 도달
        if x == t:
            # 걸린 시간 출력
            print(distance[x]-1)
            path = [t]
            temp = t
            for i in range(distance[t]-1):
                path.append(move[temp])
                temp = move[temp]
            return path
        for nx in (x+1, x-1, 2*x):
            if 0 <= nx < 100001 and distance[nx] == 0:
                distance[nx] = distance[x] + 1
                # nx에 오기전에 거쳐온 x 저장
                move[nx] = x
                queue.append(nx)

s, t = map(int, input().split())
distance = [0] * 100001
move = [False] * 100001
path = bfs()
# 역순으로 출력
path.reverse()
for i in path:
    print(i, end=' ')
