from collections import deque

N,M = map(int, input().split())

maps = [[] for _ in range(N+1)]

def bfs():
    v = [0] * (N+1)
    q = deque()
    q.append(1)
    v[1] = 1
    while q:
        qs = q.popleft()
        for i in maps[qs]:
            if v[i] == 0:
                v[i] = v[qs]+1
                if i == N:
                    break
                q.append(i)
    if v[must_go[0]] >= 1 and v[must_go[1]] >= 1:
        return 1
    return -1




far = []
for _ in range(M):
    a,b,c, = map(int ,input().split())
    maps[a].append(b)
    maps[b].append(a)
    far.append((a,b,c))

must_go = list(map(int, input().split()))
ret = bfs()
tmp0 = []
tmp1 = []
tmpN = []
if ret == -1:
    print(-1)
else:
    for i in far:
        if i[1] == must_go[0]:
            tmp0.append(i[2])
        elif i[1] == must_go[1]:
            tmp1.append(i[2])
        elif i[1] == N:
            tmpN.append(i[2])
    print(min(tmp0)+min(tmp1)+min(tmpN))