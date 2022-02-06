# 1929번 소수 구하기
# 여러개의 소수를 구하기에 에라토스테네스의 체 알고리즘 사용
import math

M, N = map(int, input().split())
arr = [True for i in range(N+1)]
arr[1] = 0

for i in range(2, int(math.sqrt(N))+1):
    if arr[i] == True:
        j = 2
        while i * j <= N:
            arr[i*j] = False
            j += 1

for num in range(M, N+1):
    if arr[num]:
        print(num)
