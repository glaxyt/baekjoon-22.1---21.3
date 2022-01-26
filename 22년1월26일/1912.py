# 1912번 연속합
N = int(input())
arr = list(map(int, input().split()))
sel_max = []
for i in range(N-1):
    sel_max.append(arr[i]+arr[i+1])
print(max(sel_max)) 
