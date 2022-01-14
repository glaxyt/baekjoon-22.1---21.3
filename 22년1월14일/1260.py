# 1260 DFS, BFS 동시 사용
import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 라이브러리 deque사용
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)     # dfs와 달리 append를 추가해줘서 while문 유지
                visited[i] = True

vertex, edge, v = list(map(int, input().split()))
graph = []
visited_dfs = [False] * (vertex+1) # visited가 안겹치게 2개 생성
visited_bfs = [False] * (vertex+1)

for i in range(vertex+1):        # bfs와 dfs에 이용할 graph생성
    graph.append([])

for i in range(edge):            # 주어진 input을 배열 graph에 추가
    first, second = input().split()
    graph[int(first)].append(int(second))
    graph[int(second)].append(int(first))

for i in range(1, vertex+1):     # bfs를 위해 정렬
    graph[i] = sorted(graph[i])

dfs(graph, v, visited_dfs)
print()     # 줄바꿈
bfs(graph, v, visited_bfs)
