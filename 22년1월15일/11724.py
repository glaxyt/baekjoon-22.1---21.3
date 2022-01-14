# 11724번 사이클 개수 구하기
import sys
sys.setrecursionlimit(10000)        # 재귀 제한을 풀어준다.
input = sys.stdin.readline

def dfs(graph, v, visited):     # 사이클안 에 존재하는 모든 노드들을 방문해준다.
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

N, M = list(map(int, input().split()))
graph = []
visited = [0] * (N+1)
total = 0

for i in range(N+1):
	graph.append([])

for i in range(M):
    M1, M2 = list(map(int, input().split()))
    graph[M1].append(M2)
    graph[M2].append(M1)

for i in range(1, N+1):
    if visited[i] == 0:         # 한사이클을 돌았는데도 방문하지못한 노드를 찾을 수 있다.
        dfs(graph, i, visited)  # 사이클을 돌린다.
        total += 1              # 사이클 종료 total +1

print(total)
