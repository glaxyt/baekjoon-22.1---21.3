# 1325번 효율적인 해킹
# 배열 작성 bfs사용
# N = 컴퓨터, M = 간선 개수(방향있음), 시간초과 때문에 pypy3으로 제출했음
import sys
import collections
input = sys.stdin.readline

def bfs(idx):
    visited= [0 for _ in range(N+1)]
    cnt = 1
    queue = collections.deque([idx])
    visited[idx] = 1
    while queue:
        x = queue.popleft()
        for k in graph[x]:
            if visited[k] == 0:
                visited[k] = 1
                cnt += 1
                queue.append(k)
    return cnt
    

N, M = map(int, input().split())
graph = collections.defaultdict(list)

for _ in range(M):      # 배열 작성
    a, b = map(int, input().split())
    graph[b].append(a)      # a가 b를 신뢰하기에 b를 타고 a를 갈 수 있다.

number= []
largest = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if cnt > largest:
        largest = cnt
    number.append([i, cnt])

for i, value in number:
    if value == largest:
        print(i, end=' ')
    
