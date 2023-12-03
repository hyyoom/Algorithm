import sys
input = sys.stdin.readline
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]
N,M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
far_of_chicken = []

def bfs(dir):
    global far_of_chicken
    v1 = [[0]*N for _ in range(N)]
    # v = [[0]*N for _ in range(N)]
    q = deque()
    for y,x in dir:
        q.append((y,x,0))
        # v1[y][x] = 1
    sums = 0
    while q:
        y,x,count = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<N and maps[ny][nx] != 2 and v1[ny][nx] == 0:
                v1[ny][nx] = v1[y][x] + 1
                q.append((ny,nx,count+1))
            if 0<=ny<N and 0<=nx<N and maps[ny][nx] == 1 and v1[ny][nx] == 0:
                sums+=v1[ny][nx]
                far_of_chicken.append(sums)
            
dir_of_chicken = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            dir_of_chicken.append((i,j))

bfs(dir_of_chicken)
print(dir_of_chicken)
print(far_of_chicken)












