import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**4) # 재귀 너무 깊게하면 안됨. 4정도 적당

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def change_map(maps):
    tmps = [[0]*M for _ in range(N)]

    check_zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                check_zero_cnt = 0 
                for k in range(4):
                    ny = dy[k] + i
                    nx = dx[k] + j
                    if 0<=ny<N and 0<=nx<M and not maps[ny][nx]:
                        check_zero_cnt += 1
                tmps[i][j] = check_zero_cnt

    check_zero_cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                maps[i][j] = maps[i][j] - tmps[i][j]
                if maps[i][j] <= 0:
                    maps[i][j] = 0
            if maps[i][j] == 0:
                check_zero_cnt+=1
    
    if (N*M) == check_zero_cnt:
        return 1
    else:
        return 0


def dfs(i,j):
    for k in range(4):
        ny = dy[k] + i
        nx = dx[k] + j
        if 0<=ny<N and 0<=nx<M:
            if not v[ny][nx] and maps[ny][nx] != 0:
                v[ny][nx] = 1
                dfs(ny,nx)
                

year = 0
while True:
    cnt = 0
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not v[i][j] and maps[i][j] != 0:
                v[i][j] = 1
                dfs(i,j)
                cnt += 1
    if cnt >= 2:
        break
    if change_map(maps):
        year = 0
        break
    year += 1

print(year)
    