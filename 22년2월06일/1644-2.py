# 1644번 소수의 연속합
# 여러개의 소수, 투 포인터 알고리즘 사용 n의 범위 => (1 ≤ n ≤ 4,000,000)
n = int(input())
arr = [True for _ in range(n+1)]

def primes_li(N):
    for i in range(2, int(N**0.5)+1):
        if arr[i]:
            for j in range(i*2, N+1, i):
                arr[j] = False
    return [i for i in range(2, N+1) if arr[i]]

def solve(list):
    ans = 0
    end = 0
    interval_sum = 0
    for start in range(len(list)):
        while interval_sum < n and end < len(list):
            interval_sum += list[end]
            end += 1
        if interval_sum == n:
            ans += 1
        interval_sum -= list[start]
    print(ans)

primes = primes_li(n)
solve(primes)

