# 별로 산 쌓기 최종문제
# 이중포문으로 가로세로 만들기
A = int(input())

for i in range(1, 2*A):              # A층만큼 산이 쌓인다.
    for r in range(1, (2*A)):        # 층에 얼마나 별과 공백이 쌓일지 정해준다.
        if i <= A:
            if r < A+1-i:
                print(' ', end='')
            elif A+1-i <= r <= A-1+i:
                print('*', end='')
        if i > A:                   # 층이 A층을 넘어가게 되면 감소하기에 if문으로 바꾼다.
            if r <= i-A:
                print(' ', end='')
            elif i-A < r < 2*A-i+A:
                print('*', end='')
    print()
        
