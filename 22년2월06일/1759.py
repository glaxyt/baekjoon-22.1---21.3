# 1759번 암호 만들기
# combiantions 사용예정
from itertools import combinations

l, c = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
arr = input().split()
arr.sort()

for password in combinations(arr, l):
    cnt = 0
    for i in password:
        if i in vowels:
            cnt += 1
    
    if cnt >= 1 and l-cnt >= 2:
        print(''.join(password))
