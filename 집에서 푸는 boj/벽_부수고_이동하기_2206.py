from collections import deque

N,M = map(int,input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

v = [[[0]*2 for _ in range(M)] for _ in range(N)]
def bfs(y,x,wall):
    q = deque([(y, x, wall)])  # 수정된 부분: 좌표를 튜플 형태로 추가
    v[y][x][wall] = 1 # 0 == 벽 안부심
    while q:
        y,x,wall = q.popleft()
        if y == N-1 and x == M-1:
            return v[y][x][wall]
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0<=ny<N and 0<=nx<M and not v[ny][nx][wall] and maps[ny][nx] == 0:
                v[ny][nx][wall] = v[y][x][wall] + 1
                q.append((ny, nx, wall))  # 수정된 부분: 좌표를 튜플 형태로 추가
            if 0<=ny<N and 0<=nx<M and wall == 0 and maps[ny][nx] == 1:
                q.append((ny,nx,1))
                v[ny][nx][1] = v[y][x][wall] + 1

    return -1


print(bfs(0,0,0))

# chk = 0
# for i in result:
#     if i == -1:
#         chk += 1
# if chk == len(result):
#     print(-1)
# else:
#     print(max(result))