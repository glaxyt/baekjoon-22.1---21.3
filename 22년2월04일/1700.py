# 1700 멀티탭 스케줄링
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

multitab = [0] * N
plug_out = 0

for i in range(K):
    # 멀티탭에 이미 존재하는 가전제품이라면
    if arr[i] in multitab:
        continue
    # 멀티탭에 빈 곳이 있다면
    elif 0 in multitab:
        multitab[multitab.index(0)] = arr[i]
        continue
    # 멀티탭에 꽉찼고 멀티탭에 없는 가전제품을 써야한다면
    # 앞으로 안쓰이는 가전제품 혹은 앞으로 가장 나중에 사용하는 가전제품을 찾아서 뽑는다.
    else:
        left_arr = arr[i:]
        maximum = 0
        for j in multitab:
            # 만일 앞으로 사용하지 않는다면
            if j not in left_arr:
                change = j
                break
            # 가장 나중에 사용하는것을 찾아준다.
            else:
                if left_arr(j) > maximum:
                    maximum = left_arr.index(j)
                    change = j
    # 바꿀 가전제품 j를 찾아준 뒤에 다음 가전제품을 대신 넣어준다.
    multitab[multitab.index(change)] = arr[i]
    plug_out += 1

print(plug_out)
