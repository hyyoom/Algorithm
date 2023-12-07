import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def chk_fire(fire_dir):
    
    fire_dir2 = []
    for y,x in fire_dir:
        for k in range(4):
            ny = dy[k] + y
            nx = dx[k] + x
            if 0<=ny<N and 0<=nx<M and maps[ny][nx] == '.' or 0<=ny<N and 0<=nx<M and maps[ny][nx] == '@':
                maps[ny][nx] = '*'
                fire_dir2.append([ny,nx])

    return fire_dir2


def bfs(y,x,v,fire_dir,maps):
    q = deque()
    q.append([y,x,fire_dir])
    v[y][x] = 1
    
    while q:
        y,x,fire_dir = q.popleft()
        ny_fire_dir = chk_fire(fire_dir)
        for k in range(4):
            ny = dy[k] + y
            nx = dx[k] + x
            if 0>ny or 0>nx or N<=ny or M<=nx:
                return v[y][x]
            if 0<=ny<N and 0<=nx<M and maps[ny][nx] == '.' and not v[ny][nx]:                
                v[ny][nx] = v[y][x] + 1
                q.append([ny,nx,ny_fire_dir])
    return 'IMPOSSIBLE'


T = int(input())
for _ in range(T):
    M,N = map(int,input().split())
    maps = []
    for _ in range(N):
        maps.append(list(input().strip()))
    
    fire_dir = []
    for r in range(N):
        for c in range(M):
            if maps[r][c] == '*':
                fire_dir.append([r,c])
    
    for r in range(N):
        for c in range(M):
            if maps[r][c] == '@':
                v = [[0]*M for _ in range(N)]
                answer = bfs(r,c,v,fire_dir,maps)
    print(answer)