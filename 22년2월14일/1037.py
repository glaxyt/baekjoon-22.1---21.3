# 1037번 약수
import sys
input = sys.stdin.readline

_ = input().rstrip()
arr = list(map(int, input().split()))

print(max(arr)*min(arr))
