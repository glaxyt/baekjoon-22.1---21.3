# 1865번 웜홀
import sys
input = sys.stdin.readline
INF = int(1e9)

def bf():
    distance = [INF] * (n+1)
    # 시작 노드에 대해서 초기화
    distance[1] = 0
    # 전체 n번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for v, nv, w in edges:
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
            # INF인 값도 찾아준다면 간선이 이어지지않은 사이클도 발견할 수 있다.
            if distance[nv] > distance[v] + w:
                distance[nv] = distance[v] + w
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False

t = int(input())
for _ in range(t):
    n, road, wormhole = map(int, input().split())
    edges = []
    for _ in range(road):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(wormhole):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))
    if bf():
        print("YES")
    else:
        print("NO")

