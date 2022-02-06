# 1929번 소수 구하기
# 여러개의 소수를 구하기에 에라토스테네스의 체 알고리즘 사용
import math

M, N = map(int, input().split())
arr = [True for i in range(N+1)]

def prime():
    for i in range(2, int(math.sqrt(N))+1):
        if arr[i]:
            for j in range(i*2, N+1, i):
                arr[j] = False
    return [arg for arg in range(2, N+1) if arr[arg]]

def solve(list):
    for i in range(len(list)):
        if M <= list[i] <= N:
            print(list[i])

prime_li = prime()
solve(prime_li)
