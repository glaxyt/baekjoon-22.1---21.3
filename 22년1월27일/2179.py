# 2179번 계단 오르기
import sys
input = sys.stdin.readline
dp = []
arr = []
N= int(input())
for i in range(N):
    arr.append(int(input()))

if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0] + arr[1])
else:
    dp.append(arr[0])
    dp.append(arr[0]+ arr[1])
    dp.append(max(arr[0] + arr[2], arr[1] + arr[2]))
    for i in range(3, N):
        dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
    print(dp.pop())

