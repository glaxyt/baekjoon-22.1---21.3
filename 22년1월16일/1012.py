# 1012번 유기농 배추
# 인접한 부분을 하나의 독립된 개체로 본다.(인접기준은 상하좌우)
# 2차원 배열이기에 좌표가 필요하다.(M = 가로길이, N = 세로길이)
# 타겟은 주어졌다. (배추는 K개)
# bfs 사용할것이다.
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
M, N, K = map(int, input().split())


for _ in range(T):
    graph = [[0]*M for _ in range(N)] # 2차원 배열 완성
    
    for _ in range(K):      # 배추 위치를 2차원 배열에 추가
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    bfs