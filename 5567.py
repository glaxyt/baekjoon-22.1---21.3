# 5567번 
# 친구의 친구까지만 초대장을 줄 것이다.
# bfs 함수의 while문에 제한을 두어서 풀것이다.
import sys
from collections import deque
input = sys.stdin.readline

def bfs(frineds_of_1):            # with_1은 범위를 제한하는데 쓰일것임 bfs를 이용해 1의 친구 수와 1의 친구들의 친구 수만 확인하면 되기 때문
    global total
    queue = deque([1])
    visited[1] = 1
    count = 0
    while count < friends_of_1:       # 첫번째 예시를 본다면 1의 친구는 [2,3]이기에 friends_of_1은 3이다. 1, 2, 3의 친구들만 확인하면된다. 대신 중복되지않게 센다.
        l = queue.popleft()
        for i in graph[l]:
            if visited[i] == 0:       # 방문하지 못했던 동기를 보면 total +1추가
                queue.append(i)
                visited[i] = 1
                total += 1
        count += 1

N = int(input()) # 동기 수 int로 줄바꿈 \n 제거
M = int(input()) # 관계 수
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
total = 0

for i in range(M):
    M1, M2 = list(map(int, input().split()))
    graph[M1].append(M2)
    graph[M2].append(M1)

friends_of_1 = len(graph[1]) + 1          # friends_of_1은 1의 1촌 친구들과 1(본인)을 더한 수이다.
bfs(friends_of_1)

print(total)
