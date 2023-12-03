from collections import deque

N  = int(input())
people_cnt = list(map(int, input().split()))
ret  = []

def bfs(g,node):
    v = [0] * (N+1)
    q = deque()
    q.append(g[0]) # 시작 인덱스
    v[g[0]] = 1
    if g:
        cnt = people_cnt[g[0]-1]
        while q:
            p = q.popleft()
            for nq in node[p]:
                if nq in g:
                    if not v[nq]:
                        v[nq] = 1
                        q.append(nq)
                        cnt += people_cnt[nq-1]
		# print(v)
    return [cnt, v.count(1)]

def permutation(i, n, v,node):
    if i == n:
        g1 = []
        g2 = []
        for idx in range(1,n+1):
            if v[idx]:
                g1.append(idx)
            else:
                g2.append(idx)
        if g1 and g2:
            g1_cnt = bfs(g1,node)
            g2_cnt = bfs(g2,node)
            if g1_cnt[1] + g2_cnt[1] == n:
                ret.append(abs(g1_cnt[0]-g2_cnt[0]))
        return

    v[i] = 1
    permutation(i + 1, n, v, node)
    v[i] = 0
    permutation(i + 1, n, v, node)


node = [[] for _ in range(N+1)]
for i in range(1,N+1):
    data = list(map(int, input().split()))
    for j in range(1,len(data)):
        node[i].append(data[j])

v = [0]*(N+1)
permutation(1,N,v,node)

try:
	print(min(ret))
except:
    print(-1)
