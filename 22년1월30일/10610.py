# 10610번 30
# 30의 배수는 각 자리수를 더해서 3의 배수가되고 맨끝자리가 0이어야한다.
N = input()
N = sorted(N, reverse = True)
sum = 0
for i in N:
    sum += int(i)
if '0' not in N or sum % 3 != 0:
    print(-1)
else:
    print(''.join(N))
