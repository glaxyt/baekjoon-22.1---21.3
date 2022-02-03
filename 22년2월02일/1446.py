# 1446번 지름길
# 모든 좌표값의 최단거리를 저장
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
arr = []
# 입력값을 arr에 저장(리스트 형태로)
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 최단거리 초깃값 저장
dp = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i-1]+1, dp[i])
    for s, e, d in arr:
        if s == i and e <= D and dp[i]+d < dp[e]:
            dp[e] = dp[i] + d

print(dp[D])
