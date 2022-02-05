# 1476번 날짜 계산
E, S, M = map(int, input().split())
e, s, m, year= 1, 1, 1, 1

while (e, s, m) != (E, S, M):
    e += 1
    if e == 16:
        e = 1
    s += 1
    if s == 29:
        s = 1
    m += 1
    if m == 20:
        m = 1
    year += 1

print(year)
