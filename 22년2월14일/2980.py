# 2980번 도로와 신호등
import sys
input = sys.stdin.readline

cur_dis = 0
ans = 0
n, l = map(int, input().split())
for _ in range(n):
    d, r, g = map(int, input().split())
    
    ans += (d - cur_dis)
    cur_dis = d

    if ans % (r+g) <= r:
        ans += (r - (ans % (r+g)))

ans += (l - cur_dis)
print(ans)
