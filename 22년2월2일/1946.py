# 1946 신입사원
# T = 테스트 케이스, N = 인원 수
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    li = []
    answer = 1

    for i in range(N):
        li.append(list(map(int, input().split())))

    # o(n^3) 계산 막기 위해 sort로 서류순위부터 계산
    li.sort()
    max = li[0][1]
    for i in range(1, N):
        # 적어도 하나는 다른 지원자를 이겨야 하기에 면접순위에서 가장 낮은 지원자와 순위 비교
        if li[i][1] < max:
            answer += 1
            max = li[i][1]
    
    print(answer)
