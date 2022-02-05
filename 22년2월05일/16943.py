# 16943번 차이를 최대로
# 파이썬 라이브러리 중에 순열이 있기에 사용
import sys
import itertools
input = sys.stdin.readline

a, b = input().split()
b = int(b)
# 순열 사용 a_nums는 이제 a로 만들 수 있는 모든 숫자가 담긴 리스트다.
a_nums = list(map(''.join, list(itertools.permutations(a))))
maximum = -1

for num in a_nums:
    first = num[0]
    num = int(num)
    if b >= num and first != '0':
        maximum = max(maximum, num)

print(maximum)

