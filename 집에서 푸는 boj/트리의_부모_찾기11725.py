import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
node = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

v = [0] * (N+1)

ans = [[] for _ in range(N+1)]

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1
    while q:
        now = q.popleft()
        for i in node[now]:
            if not v[i]:
                v[i] = 1
                ans[i].append(now)
                q.append(i)

bfs(1)
for i in range(2, len(ans)):
    print(ans[i][0])