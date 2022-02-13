# 10798번 세로읽기
import sys
input = sys.stdin.readline
graph = [[False]*15 for _ in range(5)]

for i in range(5):
    word = list(input().rstrip())
    for j in range(len(word)):
        graph[i][j] = word[j]

for i in range(15):
    for k in range(5):
        if graph[k][i]:
            print(graph[k][i], end='')
