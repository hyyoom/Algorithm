import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

v = [[0] * M for _ in range(N)]


def bfs(y,x):
    q = deque()
    q.append((y,x))
    maps[y][x] = 0
    v[y][x] = True
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M and v[ny][nx] == 0 and maps[ny][nx] != 0:
                v[ny][nx] = 1
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny,nx))


for i in range(N):
    for j in range(M):
        if maps[i][j] != 0 and v[i][j] == 0 and maps[i][j] == 2:
            idx_i = i
            idx_j = j
            bfs(i,j)
            break

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            if abs(i-idx_i) > 1 or abs(j-idx_j) > 1:
                maps[i][j] = -1

for i in maps:
    print(*i)