# 4796번 캠핑 
# 1 < L < P < V
i = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        i += 1
        Q = L*(V // P)
        D = min(V % P, L)
        print(f'Case {i}: {Q + D}')
