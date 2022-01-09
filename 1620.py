import sys
input = sys.stdin.readline
number, question = map(int, input().split())
list_pkm = []
dict_pkm = {}

for k in range(number):
    pkm = input().rstrip()
    list_pkm.append(pkm)
    dict_pkm[pkm] = k + 1
    
for _ in range(question):
    i = input().rstrip()
    if i.isdigit():
        print(list_pkm[int(i)-1])
    else:
        print(dict_pkm[i])
