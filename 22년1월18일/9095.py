# 9095번 1, 2, 3 더하기
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for k in range(4, 11):
    dp[k] = dp[k-1] + dp[k-2] + dp[k-3]


for i in range(int(input())):
    print(dp[int(input())])
