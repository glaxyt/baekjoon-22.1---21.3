# 14501번 퇴사
import sys
input = sys.stdin.readline

T = int(input())

time = []
money = []
dp = [0]*(T+1)

for _ in range(T):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)

for k in range(T-1, -1, -1):
    if time[k] + k > T: # 남은시간보다 많이 남았다면 이전에 저장한 dp가 최대
        dp[k] = dp[k+1]
    else:
        dp[k] = max(dp[k+1], money[k] + dp[k+time[k]])  # k => 현재 날짜, dp[k+time[k]] => 현재날짜 + 상담하느라 소모해야하는 시간

print(dp[0])
