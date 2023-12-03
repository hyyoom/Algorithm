import sys

# input = sys.stdin.readline
sys.stdin = open("./test.txt", "r")
sys.setrecursionlimit(10**6)
answer = 0

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def dfs(r,c,v):
    global answer
    if maps[r][c] == 'E':
        flag = 0
        for p in point:
            if not v[p[0]-1][p[1]-1]:
                flag = 1
                break
        
        for i in range(1,M-1):
            if v[point[i][0]-1][point[i][1]-1] > v[point[i+1][0]-1][point[i+1][1]-1]:
                flag = 1
                break
        
        # for m in maps:
        #     print(m)
        # print()
        
        if not flag:
            answer += 1
        return
    for k in range(4):
        nr = dr[k] + r
        nc = dc[k] + c
        if 0<=nr<N and 0<=nc<N and maps[nr][nc] in [0,'E',2] and maps[nr][nc] != 'S' and not v[nr][nc]:
            v[nr][nc] = v[r][c]+1
            dfs(nr,nc,v)
            v[nr][nc] = 0
            # if maps[nr][nc] != 2:
            #     v[nr][nc] = 0
                
N,M = map(int,input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
point = [list(map(int, input().split())) for _ in range(M)]

if not maps[point[0][0]-1][point[0][1]-1]:
    maps[point[0][0]-1][point[0][1]-1] = 'S'
if not maps[point[M-1][0]-1][point[M-1][1]-1]:
    maps[point[M-1][0]-1][point[M-1][1]-1] = 'E'
for i in range(1,M-1):
    if not maps[point[M-1][0]-1][point[M-1][1]-1]:
        maps[point[i][0]-1][point[i][1]-1] = 2

v = [[0]*N for _ in range(N)]

v[point[0][0]-1][point[0][1]-1] = 1
cnt = 0
for i in range(N):
    for j in range(N):
       if maps[i][j] == 1:
           cnt += 1

if cnt == N*N:
    print(0)
else:
    dfs(point[0][0]-1,point[0][1]-1,v)
    print(answer)