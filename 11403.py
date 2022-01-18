# 11403번 경로 찾기
# 변이 N인 정사각형 배열 시작점 없음 배열을 잘만들어줘야한다.
# 1차원 배열로 바꿔주어서 간선이동이가능한지 알아보기. dfs로 풀어볼예정
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(graph, start, target):
    visited[start] = 1
    for i in graph[start]:
        if i == target:
            return 1
        if visited[i] == 0:
            dfs(graph, i, target)
    return 0


N = int(input())
graph = [[] for i in range(N+1)]

for i in range(N):
    args = list(map(int, input().split()))
    for j in range(N):
        if args[j] == 1:
            graph[i+1].append(j+1)

for y in range(N):
    for x in range(N):
        visited = [0 for i in range(N+1)]
        print(dfs(graph, y, x), end=' ')
    print()
