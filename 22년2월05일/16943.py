# 16943번 차이를 최대로
# 파이썬 라이브러리 중에 순열이 있기에 사용
import sys
from itertools import permutations
input = sys.stdin.readline

a, b = input().split()
b = int(b)
maximum = -1

# 순열 사용 a_nums는 이제 a로 만들 수 있는 모든 숫자가 담긴 리스트다.
# permutations( ) 사용 시 a는 ex) a = "1234" 일 경우
# permutations(a)의 일부는('1', '2', '3', '4')의 형태가 된다.
a_nums = []
for i in permutations(a):
    a_nums.append(''.join(i))

for num in a_nums:
    if num[0] == '0':
        continue
    num = int(num)
    if b > num:
        maximum = max(maximum, num)

print(maximum)

