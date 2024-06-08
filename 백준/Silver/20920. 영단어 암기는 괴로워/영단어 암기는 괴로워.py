import sys
input = sys.stdin.readline


N, M = map(int, input().split())

dic = dict()

for _ in range(N):
    tmp = input().strip()
    if len(tmp) >= M:
        if tmp not in dic:
            dic[tmp] = 1
        else:
            dic[tmp] += 1

dic = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]) ,x[0]))

for r in dic:
    print(r[0])