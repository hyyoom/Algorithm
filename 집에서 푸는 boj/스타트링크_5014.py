from collections import deque

F,S,G,U,D = map(int, input().split())
v = [0] * (2000001)


def bfs():
    # s==g return
    # U, D만큼 하고
    v[S] = 1
    q = deque()
    q.append(S)
    while q:
        p = q.popleft()
        if p == G:
            return v[p]-1
        for i in (p+U, p-D):
            if 0<i<=F and not v[i]:
                v[i] = v[p] + 1
                q.append(i)
    return 0
tmp = bfs()
if S == G:
    print(0)
elif not tmp:
    print("use the stairs")
else:
    print(tmp)