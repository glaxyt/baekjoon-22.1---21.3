# 1051번 숫자 정사각형
N, M = map(int, input().split())
rect = [list(map(int, input())) for _ in range(N)]
maximum = [1]

def check(j ,k, com):
    if rect[i+k-j][j] == rect[i+k-j][k] and com == rect[i+k-j][j]:
        return (k-j+1)**2
    else:
        return 0

for i in range(N):
    for j in range(M-1):
        for k in range(j+1, M):
            if rect[i][j] == rect[i][k]:
                if (k - j) <= (N-i-1):
                    maximum.append(check(j, k, rect[i][j]))
                    
print(max(maximum))
