# 11403번 경로 찾기
# 변이 N인 정사각형 배열 시작점 없음 배열을 잘만들어줘야한다.
# 1차원 배열로 바꿔주어서 간선이동이가능한지 알아보기. dfs로 풀어볼예정
# 방향을 갖고있는 간선이기에 2차원 배열과 달리 순환 사이클이 아닐 수도 있다. 사이클인지 아닌지 분명히 해야한다.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


N = int(input())
graph = [[] for i in range(N+1)]

for i in range(N):
    args = list(map(int, input().split()))
    for j in range(N):
        if args[j] == 1:
            graph[i+1].append(j+1)

for y in range(1, N+1):
    visited = [0 for i in range(N+1)]
    dfs(y)
    for x in range(1, N+1):     # 목표값에 방문기록이 있다면 1로 출력
        if visited[x] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
