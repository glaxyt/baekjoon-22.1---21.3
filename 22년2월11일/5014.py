# 5014번 스타트링크 
from collections import deque

floor, start, target, u, d = map(int, input().split())
visit = [0] * (floor+1)
visit[0] = 1
dx = [u, -d]

def bfs():
    queue = deque()
    queue.append(start)
    visit[start] = 1
    while queue:
        x = queue.popleft()
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx <= floor and visit[nx] == 0:
                visit[nx] = visit[x] + 1
                queue.append(nx)
    return visit[target]

ans = bfs()

if ans == 0:
    print("use the stairs")
else:
    print(ans-1)
