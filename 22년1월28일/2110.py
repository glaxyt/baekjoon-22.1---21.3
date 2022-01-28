# 2110번 공유기 설치
# 수직선 위에서 이뤄진다. N: 집 개수, C: 공유기 개수
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()

start = 1                               # 집과 집사이가 인접할 수 있는 최소거리(주어진 집들 중에 1차이 나는 집들이어도 상관x)
end = arr[-1] - arr[0]                  # 주어진 집들의 위치에서 인접할 수 있는 최대거리
answer = 0

while start <= end:                     # 공유기를 배치할 거리를 알아낼 for문 교차 시 중지.
    mid = (start + end) // 2
    cnt = 1                             # 어떠한 간격으로 공유기를 설치를 할 수 있는 공유기 개수(앞 집은 설치하고 시작한다 +1)
    current = arr[0]                    # 앞 집부터 설치
    for i in range(1, len(arr)):
        if arr[i] >= mid + current:     # 주어진 간격만큼 차이나는 집이 몇개가 있는지 확인중.
            cnt += 1
            current = arr[i]

    if cnt >= C:        # 주어진 간격으로는 빽빽하게 설치가 가능하거나 너무 널널할 경우 이전의 간격 초과로 범위를 줄여준다.
        start = mid + 1
        answer = mid
    else:               # 주어진 간격으로는 설치 할 수 없는 경우 이전의 간격 미만으로 범위를 줄여준다
        end = mid - 1
print(answer)
