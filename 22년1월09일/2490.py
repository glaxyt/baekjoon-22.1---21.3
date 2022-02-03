for _ in range(3):
    game = input().split()
    count_0 = game.count('0') # 0 개수를 알면 1 개수는 자동으로 정해진다.
    if count_0 == 1:
        print('A')
    elif count_0 == 2:
        print('B')
    elif count_0 == 3:
        print('C')
    elif count_0 == 4:
        print('D')
    else:
        print('E')
