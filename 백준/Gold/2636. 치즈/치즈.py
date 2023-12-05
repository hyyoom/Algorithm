import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]


N, M = map(int,input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))


def bfs(y,x):
    q = deque()
    q.append([y,x])
    v = [[0]*M for _ in range(N)]
    v[y][x] = 1
    melt = []
    
    while q:
        y,x = q.popleft()
        for k in range(4):
            ny = dy[k] + y
            nx = dx[k] + x
            if 0<=nx<M and 0<=ny<N:
                if not maps[ny][nx] and not v[ny][nx]:
                    v[ny][nx] = 1
                    q.append([ny,nx])
                elif maps[ny][nx] == 1 and not v[ny][nx]:
                    v[ny][nx] = 1
                    maps[ny][nx] = 2
                    melt.append([ny,nx])
    
    cheese_cnt = 0
    for r in range(N):
        for c in range(M):
            if maps[r][c] != 0:
                cheese_cnt += 1
    return cheese_cnt
time = 1
chk = [[] for _ in range(1000)]


while True:
    cheese_cnt2 = bfs(0,0)
    chk[time] = cheese_cnt2
    if cheese_cnt2 == 0:
        break
    for r in range(N):
        for c in range(M):
            if maps[r][c] == 2:
                maps[r][c] = 0
    time += 1
print(time-1)
print(chk[time-1])


