from collections import deque

N,M = map(int, input().split())

node = [[] for _ in range(N+1)]
v = [[] for _ in range(N+1)]
cow = [[] for _ in range(N+1)]
ret = []

def bfs(s, g):
    sums = 0
    q=deque()
    q.append(s)
    v[s] = 1
    while q:
        p = q.popleft()
        if p == g:
            ret.append(sums)
        for nq in node[p]:
            if not v[nq]:
                v[nq] = 1
                # sums += cow[nq][1]
                q.append(nq)



for i in range(M):
    a,b,c = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
    cow[a].append([b,c])
    cow[b].append([a,c])


for s in range(len(node[1])):
    bfs(node[1][s],N)

print(cow)
print(ret)



