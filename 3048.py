N_number, M_number = map(int, input().split())
N = list(input())       # 배열을 쓰는게 편해서 배열로 작성
N = N[::-1]             # ABC를 CBA로 N+M을 리스트로 나타냈을 때 눈으로 두 개미 그룹이 만나는 것을 확인 할 수 있게 나타낸다.
M = list(input())
T = int(input())
ants = N+M
ants.insert(0, '*')       # 끝으로 가게된 N그룹 요소의 index가 리스트 밖의 인덱스와 비교함으로 일어나는 오류를 방지하기 위해 작성 
ants.insert(len(ants), '*')

for i in range(T):
    for ant_N in N:                 # 앞그룹의 개미들이 다른그룹의 개미들과 만났는지만 확인
        k = ants.index(ant_N)       # 시간복잡도를 위한 변수 생성
        if ants[k + 1] in M:        # N그룹의 개미 앞에(인덱스 + 1) M그룹의 개미가 있을 경우 자리를 바꿔준다.
            ants[k] = ants[k+1]     # 인덱스를 이용해 반대방향으로 가는 개미를 만나면 자리를 바꿔준다
            ants[k+1] = ant_N
print(''.join(ants).strip('*'))     # 문자열로 바꿔준 뒤 strip으로 *을 없애준다.
