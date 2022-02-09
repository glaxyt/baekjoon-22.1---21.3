# 6603 로또
from itertools import combinations as comb

while True:
    numbers = input().split()
    if numbers[0] == '0':
        break
    else:
        numbers = numbers[1:]
        for i in comb(numbers, 6):
            print(' '.join(list(i)))
    print()
