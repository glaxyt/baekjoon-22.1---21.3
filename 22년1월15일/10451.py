# 10451번
# 사이클 구분 방법 시작한 수가 다시 자신을 만나면 사이클 개수 +1 dfs 사용 예정(이 문제에서 각 노드는 한 간선 밖에 가지지않기 때문에 가능)
# sys.setrecursionlimit() 함수에 대해서 알아두자.(재귀 횟수 제한을 넓히는데 쓰일 수 있음)
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited_dfs[v] = True
    next = graph[v]
    if visited_dfs[next] == False:
        dfs(next)


T = int(input().rstrip())           # 테스트 케이스 개수

for i in range(T):                  # 변수 작성 및 매 테스트케이스마다 초기화
    total = 0                       # 사이클의 개수
    N = int(input().rstrip())       # 정수 N개
    graph = [0] + list(map(int, input().split()))      # dfs에 사용할 graph틀 작성
    visited_dfs = [False] * (N+1)   # 노드 방문여부 기록할 리스트
    for i in range(1, N+1):
        if visited_dfs[i] == False:
            dfs(i)
            total += 1              # 탐색을 마쳤기에 total +1
    print(total)

