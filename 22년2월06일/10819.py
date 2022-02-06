# 10819번 차이를 최대로
# 라이브러리 itertools의 순열 이용
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
maximum = 0

for nums in permutations(arr, N):
    total = 0
    for i in range(N-1):
        total += abs(nums[i] - nums[i+1])
    if total > maximum:
        maximum = total

print(maximum)
