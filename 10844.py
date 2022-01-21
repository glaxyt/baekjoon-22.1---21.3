# 10844번 쉬운 계단
# 쉬운계단 1 <= N <= 100
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(101)]      # dp 테이블 작성

for i in range(1, 10):         # dp 테이블의 길이가 1인 값 작성.
    dp[1][i] = 1

for i in range(2, 101):
    for k in range(10):
        if k == 0:
            dp[i][k] = dp[i-1][1]
        elif k == 9:
            dp[i][k] = dp[i-1][8]
        else:
            dp[i][k] = dp[i-1][k+1] + dp[i-1][k-1]
print(sum(dp[n]) % 1000000000)