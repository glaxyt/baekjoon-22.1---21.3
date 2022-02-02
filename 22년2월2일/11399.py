# 11399번 ATM
# 제일 적은 수가 가장 많이 더해져야한다.
N = int(input())
num = list(map(int, input().split()))
num.sort()
count = 0
answer = 0
for i in num:
    count += i
    answer += count
print(answer)