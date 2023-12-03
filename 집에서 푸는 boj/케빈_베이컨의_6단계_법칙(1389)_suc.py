import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)


def bfs(s, v):
	q = deque()
	q.append(s)
	v[s] = 1
	while q:
		n = q.popleft()
		for nq in node[n]:
			if not v[nq]:
				v[nq] = v[n]+1
				q.append(nq)

ret = []
for i in range(1, N+1):
    v = [0] * (N+1)
    bfs(i,v)
    ret.append(sum(v))
print(ret.index(min(ret)) + 1)