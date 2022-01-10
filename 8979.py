# 처음 문제를 보았을 때, 어떻게 등수를 메길 것인지 고민이 됐습니다.
# 금메달을 받을 시에 A를 은메달은 B를 동메달은 C를 추가하여 문자열을 만들어서 개수를 비교해서
# 리스트에서 등수를 메기겠습니다.
number, question = map(int, input().split())
nation = {}
rank = []
for i in range(number):
    args = input().split()
    nation[args[0]] = list(args[1:])

for i in range(nation):