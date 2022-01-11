# 총감독관, 부감독관 사람 수 파악하
import sys
input = sys.stdin.readline

test = int(input())      # 시험장 개수, int화 시켜서 줄 개행(이스케이프 코드) 제거
students = list(map(int, input().split()))    # 각 시험장마다 응시생 수를 받는 리스트
main_sup, sub_sup = map(int, input().split())  # 감독관과 부 감독관이 감시할 수 있는 응시생 수
total = 0               # 부 감독관 수 계산
idx = 0                 # students의 완전탐색을 위한 인덱스

for arg in students:
    if arg <= main_sup:             # 만일 총감독관 한명으로 가능하다면 아래 코드 실행 불필요
        total += 1
        continue
    students[idx] = arg - main_sup  # 시험장마다 총감독관이 무조건 있어야한다. main_sup 빼준다.
    if (students[idx] % sub_sup) != 0: # 학생 수를 sub_sup로 나누었을 때 나머지가 생기는 경우
        total += ((students[idx] // sub_sup) + 2) # 나머지를 감독해줄 감독관이 필요하기에 1명, 총감독관 1명 추가
    else:
        total += (students[idx] // sub_sup + 1) # 총감독관 추가
    idx += 1

print(total) # 시험장 개수(총감독관 수) + 부감독관 수
