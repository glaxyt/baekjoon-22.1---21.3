# 예제4-1 상하좌우
# n은 그냥 따로 받기로 함 굳이 for문열어서 시간복잡도 증가시키고 싶지않음.
n = int(input())
orders = input().split() # oreder을 str로 받아서 리스트화 시킬것이기에 이러면 됨
x, y = 1, 1

for order in orders:
    if order == 'L':
        if y != 1:
            y -= 1
    elif order == 'R':
        if y != n:
            y += 1
    elif order == 'U':
        if x != 1:
            x -= 1
    else:
        if x != n:
            x += 1

print(x, y)



