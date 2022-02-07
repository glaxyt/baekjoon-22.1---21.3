# 1963번 소수 경로
# 숫자를 바꾸는 과정에서도 네자리숫자임을 유시해야하며 소수여야한다.
from collections import deque

# 에라토스테네스의 체 알고리즘
def prime(list):
    for i in range(2, 100):
        if list[i]:
            for j in range(i*2, 10000, i):
                list[j] = False
    return list

def bfs(prime, start, end):
    queue = deque()
    queue.append(start)
    visited = [0] * 10000
    visited[start] = 1
    while queue:
        x = queue.popleft()
        str_x = str(x)
        if x == end:
            return visited[x]
        for i in range(4):
            for j in range(10):
                nx = int(str_x[:i] + str(j) + str_x[i+1:])
                if prime[nx] == True and visited[nx] == 0 and nx >= 1000:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)
    return "Impossible"

def solve():
    arr = [True for _ in range(10000)]
    prime_li = prime(arr)
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        print(bfs(prime_li, a, b)-1)

solve()
