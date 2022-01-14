# 2606번 문제 DFS(깊이 우선 탐색) 사용
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    global result         # result 글로벌 선언
    visited[v] = True
    result += 1           # 컴퓨터에 연결되어있다면, result에 추가
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

num = int(input().rstrip())
graph = []                  # BFS를 쓸 배열
visited = [False] * (num+1) # BFS를 실행할 배열 생성 인덱스가 0인 리스트는 공백인리스트로 추가하기위해 num+1개 생성
result = 0

for i in range(num+1):        # BFS를 실행할 배열 생성 인덱스가 0인 리스트는 공백인리스트로 추가하기위해 num+1개 생성
    graph.append([])

for i in range(int(input().rstrip())):      # 배열 graph 완성
    first, second = input().split()
    graph[int(first)].append(int(second))
    graph[int(second)].append(int(first))

dfs(graph, 1, visited)

print(result-1) # 컴퓨터 1 본인을 제외하고 연결된 컴퓨터 수가 결과값