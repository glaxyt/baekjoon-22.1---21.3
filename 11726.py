# 11726번 2xn 타일링
# 동적 계획법 사용 1 <= n <= 1000
# bottom-up 방식 사용(DP 테이블)
n = int(input())
dp = [0] * 1001     # DP 테이블
dp[1] = 1
dp[2] = 2

for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)