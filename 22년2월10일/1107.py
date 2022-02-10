# 1107번 리모컨
# 최소버튼 수 구하기. 숫자버튼으로 근삿값까지 도달
from collections import deque
import sys
input = sys.stdin.readline

def check(n, numbers):
    # 방향키로만 채널을 맞추는 경우
    least_cnt = abs(n - 100)
    # n의 근삿값을 찾기위해 완전탐색
    for i in range(1000000):
        for j in range(len(str(i))):
            if str(i)[j] not in numbers:
                break
            # i를 완전히 만들 수 있다면 비교해본다.
            elif j == len(str(i)) - 1:
                least_cnt = min(least_cnt, abs(n-i) + len(str(i)))
    print(least_cnt)

def solve():
    n = int(input())
    t = int(input())
    numbers = {str(i) for i in range(10)}
    # 리모컨 완성
    if t != 0:
        numbers -= set(map(str, input().split()))
    check(n, numbers)

solve()
