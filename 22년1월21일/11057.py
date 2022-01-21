# 11057번 오르막 수
# 오르막 길이 1 <= n <= 1000
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(1001)]      # dp 테이블 작성

for i in range(10):         # dp 테이블의 길이가 1인 값 작성.
    dp[1][i] = 1

for i in range(2, 1001):    # n-1자리에서 끝자리가 k인 값까지 개수의 합
    for k in range(10):
        for j in range(k+1):
            dp[i][k] += dp[i-1][j]

print(sum(dp[n]) % 10007)
