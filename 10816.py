from sys import stdin
_ = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
_ = stdin.readline()
M = map(int, stdin.readline().split())

def binary(n, N, start, end):
    if start > end: return 0
    m = (start + end) // 2
    if N[m] == n:
        return N[start:end+1].count(n) # 바로 발견했기에 완전탐색
    elif N[m] > n:
        return binary(n, N, start, m-1)  # 인덱스를 고쳐서 리스트 N의 탐색구역을 조정
    else:
        return binary(n, N, m+1, end) # 인덱스를 고쳐서 리스트 N의 탐색구역을 조정

n_dict = {}
for n in N:
    start = 0
    end = len(N)-1
    if n not in n_dict:
        n_dict[n] = binary(n, N, start, end)
print(' '.join(str(n_dict[x]) if x in n_dict else '0' for x in M))
