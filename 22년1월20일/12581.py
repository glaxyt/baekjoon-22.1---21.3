# 12581번 숨바꼭질
# 이동방향 [+1, -1, 2*x] 걸리는 시간은 각각 동일하다. 
# 최단시간과 최단시간으로 가는 방법의 개수를 출력하라(줄바꿈으로 출력)
# 최단시간은 계산가능.
import sys
from collections import deque
input = sys.stdin.readline

graph = [0] * 100001
cnt = [0] * 100001
N, K = map(int, input().split())
queue = deque([N])

def bfs():
    graph[N] = 1
    while queue:
        x = queue.popleft()
        for i in [+1, -1, x]:
            nx = x + i
            if 0 <= nx < 100001 and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)
            elif 0 <= nx < 100001 and graph[nx] != 0:
                if graph[nx] == graph[x] + 1:       # 다른방법으로 왔는데 최단시간이 같다면.
                    queue.append(nx)                # 최단시간이 같기에 여기서도 다시 돌려준다.
                    cnt[nx] += 1                    # 방법 +1을 추가

bfs()
print(graph[K]-1)   # 시작값이 1이기에 1을 빼줘야한다.
print(cnt[K]+1)     # 첫방문 + 이후방문이기에 첫방문 +1
# print(최단시간 - 1) 
# cnt는 최단시간으로 가는 방법의 수를 정렬
