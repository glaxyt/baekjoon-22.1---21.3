# 실전문제2
location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1      # 행은 숫자로 표현이 되지만, 열은 알파벳이라 까다로워서 숫자로 바꿔준다

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
