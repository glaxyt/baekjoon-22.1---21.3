n = int(input())
word = input()
n_divide = n / 5

for i, index in enumerate(word[:n_divide]):
    for r in range(4):
        if i == '#':
