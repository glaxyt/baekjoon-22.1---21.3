# 1931번 회의실 배정
# 1, 가장 빨리 끝나는 강의 우선으로 정렬 2, 가장빨리 시작하는 강의로 정렬
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort(key = lambda x:(x[1],x[0]))

cnt = 0
end = 0
for s, t in arr:
    if s >= end:
        cnt += 1
        end = t
print(cnt)
