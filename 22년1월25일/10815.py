# 10815번 숫자 카드
n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
_ = int(input())
compare = list(map(int, input().split()))

for i in compare:
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == i:
            print(1, end =' ')
            break
        elif nums[mid] > i:
            end = mid-1
        else:
            start = mid+1
    if nums[mid] != i:
        print(0, end=' ')
