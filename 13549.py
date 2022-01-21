# 13549번 숨바꼭질 3
# 이동방향 [x+1, x-1, 2*x] 대신 시간소모는 [+1, +1, 0]이다.
# 가장 빠른시간.
from collections import deque
n, k = map(int, input().split())
queue = deque([n])
visited = [0] * (1000001)
visited[n] = 1
while queue:
    x = queue.popleft()
    if x == k:
        print(visited[x])
        break
    if 0 <= 2*x <= 100001 and visited[2*x] == 0:
        visited[2*x] = visited[x]
        queue.appendleft(2*x)           # 최소시간을 찾는것이기에 2*x는 queue에서 최우선으로 실행시켜준다.
    if 0 <= x+1 <= 100001 and visited[x+1] == 0:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)
    if 0 <= x-1 <= 100001 and visited[x-1] ==0:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)