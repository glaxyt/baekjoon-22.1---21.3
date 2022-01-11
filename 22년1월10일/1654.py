# 백준 1654
# K개의 다른길이를 가진 전선들을 N개의 일정한 길이의 전선들로 만들어야한다.
# 가장 작은 길이의 전선으로 모든 전선을 나눠 준다면 가장 작은 길이로 만들 수 있는 전선 기준으로 풀어보자
from sys import stdin
K, N =  map(int, stdin.readline().split())  # K개와 N개를 정수로 받아준다.
lis_k = []                                  # K개의 전선들을 받아줄 리스트 작성.

for i in range(K):
    lis_k.append(int(stdin.readline()))          # 전선 K개의 길이들을 lis_k에 넣어준다.

average_0 = sum(lis_k) / N

def binary(average, lis_k, N):
    print('시작')
    answer = []
    for i in lis_k:
        answer.append(i // average)
    total = sum(answer)
    
    if total  == N:
        return average

    elif total > N:
        average -= 1
        return binary(average, lis_k, N)
    
    else:
        average += 1
        return binary(average, lis_k, N)

print(binary(average_0, lis_k, N))
