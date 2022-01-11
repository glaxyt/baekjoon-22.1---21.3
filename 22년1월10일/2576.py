import sys
input = sys.stdin.readline
minimum = 101 
total = 0
for i in range(7):
    a = int(input())
    if a % 2 != 0:
        total += a
        if a < minimum:
            minimum = a
if total:
    print(total)
    print(minimum)
else:
    print(-1)

