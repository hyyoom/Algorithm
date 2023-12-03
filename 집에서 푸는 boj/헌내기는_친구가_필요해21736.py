import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N,M = map(int, input().split())
maps = [list(list(input().strip())) for _ in range(N)]

v = [[0]*M for _ in range(N)]

def bfs(y,x,maps):
    cnt = 0
    q = deque()
    q.append((y,x))
    v[y][x] = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M and not v[ny][nx] and maps[ny][nx] != "X":
                v[ny][nx] = 1
                if maps[ny][nx] == "P":
                    cnt += 1
                q.append((ny,nx))
    return cnt

for i in range(N):
    for j in range(M):
        if maps[i][j] == "I":
            ret = bfs(i,j,maps)
            
if ret == 0:
    print("TT")
else:
    print(ret)
