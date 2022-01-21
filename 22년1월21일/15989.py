# 15989번 1,2,3 더하기 4
# 0 < n <= 10000 n은 정수
T = int(input())
dp = [1] * 10001 # 테이블 생성(리스트 dp의 인덱스 0에 1이 존재해야 2를 구하는데 에러가 없다.)

for i in range(2, 10001):
    dp[i] += dp[i-2]
for j in range(3, 10001):
    dp[j] += dp[j-3]
for i in range(T):
    n = int(input())
    print(dp[n])
