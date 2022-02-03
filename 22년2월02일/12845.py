# 12845번 모두의 마블
N = int(input())
num = list(map(int, input().split()))
# 내림차순으로 정리
num = sorted(num, reverse = True)
total = 0
max = num[0]

if N == 1:
    print(max)
else:
    for i in range(1, N):
        total += (max + num[i])
    print(total)
