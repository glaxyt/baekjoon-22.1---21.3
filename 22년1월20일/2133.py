# 2133번 타일 채우기
# 1 <= n <= 30
dp = [0] * 31
dp[0] = 1
dp[2] = 3

n = int(input())
for i in range(4, n+1, 2):
    dp[i] = 3 * dp[i-2]
    for k in range(0, i-2, 2):
        dp[i] += 2 * dp[k]

print(dp[n])
