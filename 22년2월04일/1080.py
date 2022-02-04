# 1080번 행렬
# 여기서 연산은 임의의 3X3구역을 0->1 1->0으로 바꾸는 작업을 뜻한다. N = 세로 M = 가로
N, M = map(int, input().split())

first = [list(map(int, input())) for _ in range(N)]
second = [list(map(int, input())) for _ in range(N)]

def change(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            first[j][i] = 1 - first[j][i]

def check():
    for y in range(N):
        for x in range(M):
            if first[y][x] != second[y][x]:
                return False
    return True

# 연산의 개수를 담는 변수
cnt = 0
# change를 위해 범위를 N-2, M-2로 설정
for y in range(N-2):
    for x in range(M-2):
        if first[y][x] != second[y][x]:
            change(x, y)
            cnt += 1

if check():
    print(cnt)
else:
    print(-1)
