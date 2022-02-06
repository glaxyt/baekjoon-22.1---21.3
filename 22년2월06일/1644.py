# 1644번 소수의 연속합
# 여러개의 소수, 투 포인터 알고리즘 사용 N의 범위 => (1 ≤ N ≤ 4,000,000)
N = int(input())
arr = [True for i in range(N+1)]
primes = []
for i in range(2):
    arr[i] = False
for i in range(int(N**0.5)+1):
    if arr[i]:
        for j in range(i*2, N+1, i):
            arr[j] = False
            
for i in range(N+1):
    if arr[i]:
        primes.append(i)

primes_len = len(primes)
count = 0
interval_sum = 0
end = 0
for start in range(primes_len):
    while interval_sum < N and end < primes_len:
        interval_sum += primes[end]
        end += 1
    if interval_sum == N:
        count += 1
    interval_sum -= primes[start]

print(count)
