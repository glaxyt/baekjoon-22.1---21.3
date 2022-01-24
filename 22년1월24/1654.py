# 백준 1654
# K개의 다른길이를 가진 전선들을 N개의 일정한 길이의 전선들로 만들어야한다.
# 이분탐색을 위한 target, start, mid를 잡아준다. 이분탐색을 최댓값을 찾을때까지 진행된다.
import sys
input = sys.stdin.readline
K, N =  map(int, input().split())          # K개와 N개를 정수로 받아준다.
lis_k = []                                 # K개의 전선들을 받아줄 리스트 작성.
for i in range(K):
    lis_k.append(int(input()))             # 전선 K개의 길이들을 lis_k에 넣어준다.
start = 1
end = max(lis_k)

while start <= end:
    cnt = 0
    mid = (start+end) // 2 # mid는 정수여야한다.
    for i in lis_k:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1 # N이 크거나 같다면 크기를 더 늘려도된다.
    else:
        end = mid - 1 # N이 작다면 크기를 늘려서 더 잘게 잘라서 N을 늘려준다.
print(end)            # 왜 end인가? while문이 끝날때 쯤에 start와 end는 K와 K+1의 근삿값에 도달한다. 여기서 end와 start는 순서가 바뀌기에 K에 근사치인 end를 뽑는다.
