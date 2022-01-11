from sys import stdin
input = stdin.readline

def coin_calculate(K, coins):
    total = 0
    for coin in coins:
        if coin < K:                   # coins의 동전들 중 동전값이 가장 큰 동전부터 나눠준다. 문제점: 못쓰는 동전까지 탐색해서 시간낭비
            total += K // coin          # total은 K를 나눌때마다 사용된 동전 개수만큼 증가
            K = K % coin                # K를 동전으로 나눠준 후에 남은 K값 저장 다음 for문에서 사용할 예정 
    return total

N, K = map(int, input().split())
coins = []

for i in range(N):
    coins.append(int(input().rstrip())) # rstrip해줘야 \n이 없애줄 수 있다.
coins = sorted(coins)[::-1]             # 내림차순으로 정렬.


print(coin_calculate(K, coins))
