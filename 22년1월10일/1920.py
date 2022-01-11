from sys import stdin
_ = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
_ = stdin.readline()
M = map(int, stdin.readline().split())

def binary(find, N, start, end):
    if start > end: return 0
    middle = (start + end) // 2
    if N[middle] == find:
        return 1                    # 바로 발견했기에 1출력
    elif N[middle] > find:
        return binary(find, N, start, middle-1)  # 인덱스를 고쳐서 리스트 N의 탐색구역을 조정
    else:
        return binary(find, N, middle+1, end) # 인덱스를 고쳐서 리스트 N의 탐색구역을 조정

for m in M:
    start = 0
    end = len(N)-1
    print(binary(m, N, start, end))
