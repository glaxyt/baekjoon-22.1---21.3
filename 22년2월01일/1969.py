# 1969번 DNA

N, M = map(int, input().split())
DNA = []
TAGC = ['A', 'C', 'G', 'T']
answer = ''
cnt = 0
for i in range(N):
    DNA.append(input())

for k in range(M):
    TAGC_cnt = [0, 0, 0, 0]
    for j in range(N):
        if DNA[j][k] == 'A':
            TAGC_cnt[0] += 1
        elif DNA[j][k] == 'C':
            TAGC_cnt[1] += 1
        elif DNA[j][k] == 'G':
            TAGC_cnt[2] += 1
        elif DNA[j][k] == 'T':
            TAGC_cnt[3] += 1
    word = max(TAGC_cnt)
    answer += TAGC[TAGC_cnt.index(word)]
    cnt += (N - word)

print(answer)
print(cnt)
