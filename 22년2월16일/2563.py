# 2563번 색종이
n = int(input())
graph = [[0]*101 for _ in range(101)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[j][i] = 1
ans = 0
for i in graph:
    ans += sum(i)
        
print(ans)
