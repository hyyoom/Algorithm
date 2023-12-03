import sys
import copy
from collections import deque

input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

result = []

# def bfs():
#     v = [[False] * M for _ in range(N)]
#     # v[0][0] = True
#     q = deque()
#     tmp = copy.deepcopy(maps)
#     for i in range(N):
#         for j in range(M):
#             if tmp[i][j] == 2:
#                 q.append((i,j))
#     while q:
#         y,x = q.popleft()
#         for i in range(4):
#             ny = dy[i] + y
#             nx = dx[i] + x
#             if 0<=ny<N and 0<=nx<M and not v[ny][nx] and tmp[ny][nx] == 0:
#                 v[ny][nx] = True
#                 tmp[ny][nx] = 2
#                 q.append((ny,nx))

#     global answer
#     cnt = 0

#     for i in range(N):
#         cnt += tmp[i].count(0)

#     answer = max(answer, cnt)
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs():
    global answer
    # 기존 맵 정보 깊은 복사(Deep Copy)
    board_wall = copy.deepcopy(maps)
    # 바이러스 위치
    virus = [(n, m) for n in range(N) for m in range(M) if board_wall[n][m] == 2]

    # 바이러스마다 전파 끝날 때까지 반복
    while virus:
        x, y = virus.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and board_wall[nx][ny] == 0:
                board_wall[nx][ny] = 2
                virus.append((nx, ny)) # 바이러스 전파

    # 안전지대 개수 카운팅
    safezone_cnt = 0
    for row in board_wall:
        safezone_cnt += row.count(0)
    answer = max(answer, safezone_cnt)

def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for k in range(M):
            if maps[i][k] == 0:
                maps[i][k] = 1
                make_wall(count+1)
                maps[i][k] = 0

answer = 0
make_wall(0)
print(answer)

