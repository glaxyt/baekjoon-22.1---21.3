# 행은 알파벳이기에 보기편하게 행도 1-8로 바꿔준다. 돌하고 위치가 같아질때는 돌 위치를 바꿔준다.

def is_in_boundary(next_column, next_row):      # 좌표가 범위에서 벗어났는지 확인
    if 1 <= next_column <= 8 and  1 <= next_row <= 8:
        return True

King, rock, n = input().split()
row_k = int(King[1])
row_r = int(rock[1])
column_k = int(ord(King[0])) - int(ord('A')) + 1
column_r = int(ord(rock[0])) - int(ord('A')) + 1

step_abc = ['R', 'RT', 'RB', 'T', 'B', 'LT', 'L', 'LB']
steps = [(1,0), (1,1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]


for i in range(int(n)):
    order = input()
    for i in range(8):          # step_abc에서 order를 확인
        if order == step_abc[i]:
            next_row_k = row_k + steps[i][1]
            next_column_k = column_k + steps[i][0]
            if is_in_boundary(next_column_k, next_row_k): # 좌표이동 시킨 후 유효한 좌표인지 확인
                if next_column_k == column_r and next_row_k == row_r:   # 유효한 좌표로 이동시킨 킹과 돌이 만난다면
                        next_column_r = column_r + steps[i][0]
                        next_row_r = row_r + steps[i][1]
                        if is_in_boundary(next_column_r, next_row_r):   # 이동시킨 돌의 좌표가 유효한지 확인
                            row_r = next_row_r
                            row_k = next_row_k
                            column_r = next_column_r
                            column_k = next_column_k
                else:                                                   # 유효한 좌표로 이동시킨 킹이 돌과 만나지 않음
                    column_k = next_column_k
                    row_k = next_row_k
                    
print(chr(column_k + int(ord('A')) - 1), row_k, sep='')
print(chr(column_r + int(ord('A')) - 1), row_r, sep='')

