import sys
import copy
from collections import deque

input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]


def bfs(tmp):
    v = [[False] * N for _ in range(M)]
    # v[0][0] = True
    q = deque()
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i,j))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M and not v[ny][nx] and tmp[ny][nx] == 0:
                v[ny][nx] = True
                tmp[ny][nx] = 2
                q.append((ny,nx))

    return tmp
        
cnt = 0
ret = []

for i in range(N):
        for j in range(M):
            for k in range(N):
                for l in range(M):
                    for a in range(N):
                        for b in range(M):
                            if i != k and i != a and k != a and j != l and j != b and l != b:
                                if maps[i][j] == 0 and maps[k][l] == 0 and maps[a][b] == 0:
                                    tmp = copy.deepcopy(maps)
                                    tmp[i][j] = 1
                                    tmp[k][l] = 1
                                    tmp[a][b] = 1
                                    tmp = bfs(tmp)
                                    for z in tmp:
                                        cnt += z.count(0)
                                    # if cnt == 19:
                                    #     for i in tmp:
                                    #         print(i)
                                    ret.append(cnt)
                                    tmp = []
                                    cnt = 0


# for i in range(N):
#     for j in range(M):
#         maps[i][j] = 1
#         for k in range(N):
#             for l in range(j+1,M):
#                 if j != l:
#                     maps[k][l] = 1
#                     for a in range(N):
#                         for b in range(l+1,M):
#                             if (b != l) and (b != j):
#                                 if maps[i][j] == 0 and maps[k][l] == 0 and maps[a][b] == 0:
#                                     tmp = copy.deepcopy(maps)
#                                     tmp[i][j] = 1
#                                     tmp[k][l] = 1
#                                     tmp[a][b] = 1
#                                     tmp = bfs(tmp)
#                                     for z in tmp:
#                                         cnt += z.count(0)
#                                     # if cnt == 19:
#                                     #     for i in tmp:
#                                     #         print(i)
#                                     ret.append(cnt)
#                                     tmp = []
#                                     cnt = 0
print(max(ret))


