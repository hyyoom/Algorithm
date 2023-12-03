import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
ch1, ch2 = map(int, input().split())
M = int(input())

def bfs(start, end):
    v = [0] * (N+1)
    q = deque()
    q.append(start)
    while q:
        p = q.popleft()
        if start == end:
            return v[end]
        for np in node[p]:
            if not v[np]:
                v[np] = v[p] + 1
                q.append(np)
    return v

node = [[] for _ in range(N+1)]
for _ in range(M):
    parent, child = map(int, input().split())
    node[parent].append(child)
    node[child].append(parent)

v = bfs(ch1,ch2)
if not v[ch2]:
    print(-1)
else:
    print(v[ch2])