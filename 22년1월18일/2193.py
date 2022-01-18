# 2194번 이친수
# 동적 계획법 사용 1 <= n <= 90
# bottom-up 방식 사용. DP 테이블 사용
n = int(input())
dp = [0] * 91   # DP 테이블
dp[1] = 1
dp[2] = 1

for i in range(3, 91):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
