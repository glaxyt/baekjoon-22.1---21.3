# 10819번 차이를 최대로
import sys
import itertools
input = sys.stdin.readline

a, b = input().split()
b = int(b)
a_nums = list(map(''.join, list(itertools.permutations(a))))
maximum = -1

for num in a_nums:
    first = num[0]
    num = int(num)
    if b >= num and first != '0':
        maximum = max(maximum, num)

print(maximum)

