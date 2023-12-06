import sys
# sys.setrecursionlimit(10**9)


N,M = map(int,input().split())
maxv = -1


def dfs(y,x,cnt):
    # global alpha
    global maxv
    
    maxv = max(maxv,cnt)
    for k in range(4):
        ny = dy[k] + y
        nx = dx[k] + x
        if 0<=ny<N and 0<=nx<M and not maps[ny][nx] in alpha:
            alpha.add(maps[ny][nx])
            dfs(ny,nx,cnt+1)
            alpha.remove(maps[ny][nx])

maps = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]
for _ in range(N):
    maps.append(list(input()))
alpha = set()
alpha.add(maps[0][0])

dfs(0,0,1)
print(maxv)